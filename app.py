from __future__ import annotations

import logging
import os
import sys

from flask import Flask, jsonify

import config
from main import seed_all
from rust_client import RustClient
from resolver import resolve_pending

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    stream=sys.stdout,
)
logger = logging.getLogger("friendlies_standalone.app")

app = Flask(__name__)

_client: RustClient | None = None


def _get_client() -> RustClient:
    global _client
    if _client is None:
        if not config.FANCLASH_API:
            raise RuntimeError("FANCLASH_API is not set")
        _client = RustClient(config.FANCLASH_API)
    return _client


@app.get("/")
def health() -> tuple:
    # Cheap, no network call -- same as before.
    return jsonify(status="ok"), 200


@app.get("/run")
def run() -> tuple:
    try:
        client = _get_client()
        seed_all(client)
        resolve_pending(client)
    except Exception:
        logger.exception("Unhandled error during /run")
        return jsonify(status="error"), 500

    return jsonify(status="ok"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "10000")))
