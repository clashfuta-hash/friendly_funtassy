from __future__ import annotations

import logging
import os
import sys

from flask import Flask, jsonify

import config
from main import seed_all
from mongo_store import FixtureStore
from resolver import resolve_pending

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger("friendlies_standalone.app")

app = Flask(__name__)

_store: FixtureStore | None = None


def _get_store() -> FixtureStore:
    global _store
    if _store is None:
        if not config.MONGO_URI:
            raise RuntimeError("MONGO_URI is not set")
        _store = FixtureStore(config.MONGO_URI)
    return _store


@app.get("/")
def health() -> tuple:
    # Render (and most uptime checks) hit "/" -- keep it cheap, no DB call.
    return jsonify(status="ok"), 200


@app.get("/run")
def run() -> tuple:
    try:
        store = _get_store()
        seed_all(store)
        resolve_pending(store)
    except Exception:
        logger.exception("Unhandled error during /run")
        return jsonify(status="error"), 500

    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
