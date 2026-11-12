import unittest

from api import rate_limit


class RateLimitTest(unittest.TestCase):
    def test_allows_up_to_the_budget(self):
        rate_limit._hits.clear()
        allowed = [rate_limit.allow("c1") for _ in range(rate_limit.MAX_REQUESTS)]
        self.assertTrue(all(allowed))

    def test_blocks_past_the_budget(self):
        rate_limit._hits.clear()
        for _ in range(rate_limit.MAX_REQUESTS):
            rate_limit.allow("c1")
        self.assertFalse(rate_limit.allow("c1"))


if __name__ == "__main__":
    unittest.main()
