import unittest

from api import token


class RefreshTest(unittest.TestCase):
    def test_valid_token_is_returned_unchanged(self):
        tok = token.issue(7)
        self.assertEqual(token.refresh(tok), tok)

    def test_expired_token_is_reissued(self):
        stale = {"user_id": 7, "token": "tok-7", "expires_at": token.now() - 1}
        fresh = token.refresh(stale)
        self.assertTrue(token.is_valid(fresh))
        self.assertEqual(fresh["user_id"], 7)


if __name__ == "__main__":
    unittest.main()
