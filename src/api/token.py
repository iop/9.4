"""Access-token issuance and refresh."""

import time

TTL_SECONDS = 3600


def now():
    """Current timestamp in seconds."""
    return int(time.time())


def issue(user_id):
    """Issue a fresh access token for the user, valid for one hour."""
    return {
        "user_id": user_id,
        "token": "tok-%s" % user_id,
        "expires_at": now() + TTL_SECONDS,
    }


def is_valid(token):
    """True while the token has not reached its expiry."""
    return token.get("expires_at", 0) > now()


def refresh(token):
    """Return a still-valid token, re-issuing it when it has expired."""
    if is_valid(token):
        return token
    return issue(token["user_id"])
