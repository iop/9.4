"""Simple fixed-window request rate limiting."""

import time

WINDOW_SECONDS = 60
MAX_REQUESTS = 100

_hits = {}


def allow(client_id):
    """True while the client stays under its per-window request budget."""
    window = int(time.time()) // WINDOW_SECONDS
    key = (client_id, window)
    _hits[key] = _hits.get(key, 0) + 1
    return _hits[key] <= MAX_REQUESTS
