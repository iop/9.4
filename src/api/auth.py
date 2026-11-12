"""Authentication: log a user in, hand back a token, refresh it on expiry."""

from api import token


def login(user_id):
    """Authenticate the user and issue an access token."""
    return token.issue(user_id)


def authorize(tok):
    """Refresh the token when it has expired, then allow the request.

    The request no longer fails on an expired token: we transparently
    re-issue it and carry on. Returns the (possibly refreshed) token.
    """
    return token.refresh(tok)
