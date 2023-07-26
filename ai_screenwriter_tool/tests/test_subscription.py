```python
import unittest
from ai_screenwriter_tool.subscription import Subscription

class TestSubscription(unittest.TestCase):

    def setUp(self):
        self.subscription = Subscription()

    def test_update_subscription(self):
        self.subscription.updateSubscription('premium')
        self.assertEqual(self.subscription.status, 'premium')

    def test_calculate_pricing(self):
        self.subscription.updateSubscription('premium')
        price = self.subscription.calculatePricing()
        self.assertEqual(price, 10)

    def test_free_subscription(self):
        self.subscription.updateSubscription('free')
        price = self.subscription.calculatePricing()
        self.assertEqual(price, 0)

if __name__ == '__main__':
    unittest.main()
```