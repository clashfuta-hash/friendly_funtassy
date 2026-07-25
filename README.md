# wembly_friendlies_standalone

Standalone service for pre-season / Club Friendlies fixtures that 365Scores
won't surface in advance. Shares nothing code-wise with `wembly_leagues_scrapers`
or `worldcup_poller` -- the only thing shared is the Mongo `games` collection
(same `clashdb` database, same document shape), which is what lets your
existing poller pick these fixtures up automatically once resolved.

## Why this exists

365Scores' `/web/games/fixtures/` endpoint silently ignores `startDate`/`endDate`
whenever a `competitions` filter is present, so Club Friendlies (competitionId 321,
6000+ clubs worldwide pooled into one bucket) only ever returns *today's* games --
there is no reliable way to ask 365Scores "what's on in 10 days" for friendlies.

So friendlies fixtures are seeded by hand (dates/times taken from official club
announcements and press coverage, not scraped) and inserted into Mongo with no
`threesixtyfiveGameId` yet. A resolver process then watches those fixtures and,
once each one's match day actually arrives, "surrenders" control to 365Scores --
it queries 365Scores for *that specific day* (which is the one query 365Scores
answers reliably) and matches the hardcoded fixture to a real 365Scores game by
team name, writing back `threesixtyfiveGameId` + competitor ids + competition_id.
From that moment on the fixture is indistinguishable from any scraped league
fixture -- your existing `poller.py` picks it up via `store.get_all_fixtures()`
and drives it through the normal `upcoming -> soon -> live -> completed` state
machine using those same fields.

## Architecture

```
hardcoded_fixtures.py   -- the manually maintained fixture list (source of truth)
team_aliases.py         -- name variants per club, for matching against 365Scores' display names
resolver.py              -- the "midnight surrender" loop
main.py                  -- single process: seed once, then resolver.run_forever()

sources/threesixtyfive.py -- REAL, FULL copy of wembly_leagues_scrapers/sources/threesixtyfive.py
config.py                 -- REAL, FULL copy of wembly_leagues_scrapers/config.py, with a few
                              additive settings appended at the bottom (FRIENDLY_SOURCE_TAG,
                              RESOLVE_COMPETITION_IDS, RESOLVE_POLL_INTERVAL_SECONDS)
mongo_store.py             -- REAL, FULL copy of wembly_leagues_scrapers/mongo_store.py, with
                              three new methods appended to FixtureStore
                              (get_fixtures_pending_resolution, update_fixture_resolved,
                              abandon_fixture) and one new optional param (`source`) added to
                              upsert_fixture -- nothing existing was changed or removed
```

None of the above three files are reimplementations -- they're the actual files from
`wembly_leagues_scrapers`, extended in place. `resolver.py` calls the real
`threesixtyfive.fetch_games_by_date_range()`, not a bespoke single-day fetch, and
seeding goes through the real `FixtureStore.upsert_fixture()`, the same function
`leagues_scraper.py` uses for every other fixture in the collection.

### The midnight surrender

Every fixture in `hardcoded_fixtures.py` has a `kickoff_utc`. A fixture is
**eligible for resolution** once the current UTC date has reached (or passed)
its kickoff date -- i.e. at UTC midnight of match day, this repo stops trusting
the hardcoded time/date it seeded and starts asking 365Scores to confirm the
real thing (365Scores is the source of truth for the *live* game once the day
actually arrives; the hardcoded data was only ever a placeholder to get the
fixture to exist in the app ahead of time).

Each poll cycle (`RESOLVE_POLL_INTERVAL_SECONDS`, default 300s):

1. Pull every fixture from `games` where `source == "friendly_hardcoded"`,
   `threesixtyfiveGameId` is still `None`, and `kickoffUtc` date `<=` today.
2. For each, call 365Scores for that single date across every competition id
   in `RESOLVE_COMPETITION_IDS` (the friendlies bucket 321, plus league ids --
   pre-season friendlies against non-EPL/Serie A opposition sometimes get
   filed under the opponent's domestic cup id).
3. Match by team-name aliases against BOTH `homeTeam` and `awayTeam` on the
   hardcoded doc (two-sided match, not the single-side substring match
   `wembly_leagues_scrapers` uses -- friendlies pool every club on earth, so
   two-sided matching is needed to avoid false positives).
4. On a match: `update_fixture_resolved()` writes `threesixtyfiveGameId`,
   `home_competitor_id`, `away_competitor_id`, `competition_id`. Nothing else
   on the doc changes -- `status`/`isLive` stay owned by your existing poller.
5. On no match: leave it, retry next cycle. Once `kickoffUtc` + a grace window
   has fully passed with still no match, it's logged as unresolved and left
   alone (so it doesn't get re-queried forever for a friendly that got
   cancelled/rescheduled off 365Scores entirely).

### Why not just always query 365Scores for "today"?

Because 365Scores' same-day response for competition 321 alone is every
friendly on the planet that day. Two-sided team-name matching against your
own hardcoded fixture is what narrows "everyone's friendlies today" down to
"the specific one you already know is happening" -- the hardcoded fixture is
the anchor; 365Scores is only ever asked to confirm/resolve it, never to
discover fixtures on its own.

## Running it

```
pip install -r requirements.txt
cp .env.example .env   # fill in MONGO_URI
python main.py
```

Single process, single Render worker (see `render.yaml`) -- no cron, no second
service. `main.py` seeds any new entries from `hardcoded_fixtures.py` on every
boot (idempotent, upserts on `matchId`) then runs the resolver loop forever.

Note: `main.py` only calls `upsert_fixture()` for a `matchId` that doesn't already
exist (checked via `get_fixture()` first). `upsert_fixture()` writes
`threesixtyfiveGameId` into `$set` unconditionally by design, so calling it again
on a fixture the resolver has already resolved would stomp that field back to
`None` -- the existence check is what prevents that on every reboot.

## Adding fixtures

Edit `hardcoded_fixtures.py`. Each entry needs `home_team`, `away_team`,
`kickoff_utc`, `competition_name`. `matchId` is derived automatically as
`friendly_<md5(home+away+date)[:12]>` so re-running the seed is always safe.
If a club's display name on 365Scores doesn't match what you typed here,
add the variant to `team_aliases.py` -- resolution will otherwise silently
never match that fixture.
