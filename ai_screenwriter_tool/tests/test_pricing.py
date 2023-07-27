```python
import unittest
from ai_screenwriter_tool.pricing import calculatePricing
from ai_screenwriter_tool.user import User
from ai_screenwriter_tool.subscription import Subscription
from ai_screenwriter_tool.token import Token

class TestPricing(unittest.TestCase):

    def setUp(self):
        self.user = User("John Doe", "john.doe@example.com")
        self.subscription = Subscription(self.user, "free")
        self.token = Token(self.user, 0)

    def test_calculatePricing_free(self):
        self.assertEqual(calculatePricing(self.subscription, self.token), 0)

    def test_calculatePricing_premium(self):
        self.subscription.plan = "premium"
        self.assertEqual(calculatePricing(self.subscription, self.token), 10)

    def test_calculatePricing_premium_with_tokens(self):
        self.subscription.plan = "premium"
        self.token.count = 5
        self.assertEqual(calculatePricing(self.subscription, self.token), 5)

    def test_calculatePricing_invalid_plan(self):
        self.subscription.plan = "invalid"
        with self.assertRaises(ValueError):
            calculatePricing(self.subscription, self.token)

if __name__ == '__main__':
    unittest.main()
```