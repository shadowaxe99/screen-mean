```python
class Pricing:
    def __init__(self):
        self.basic_features = True
        self.premium_features = False
        self.price = 0

    def calculatePricing(self, user):
        if user.subscription:
            self.premium_features = True
            self.price = 10
        else:
            self.premium_features = False
            self.price = 0

        return self.price

    def updateSubscription(self, user, subscription_status):
        user.subscription = subscription_status
        self.calculatePricing(user)

    def checkFeatures(self):
        if self.premium_features:
            return "User has access to premium features"
        else:
            return "User has access to basic features only"
```