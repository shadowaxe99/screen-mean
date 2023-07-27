```python
from datetime import datetime
from marshmallow import Schema, fields

class Subscription:
    def __init__(self, user_id, plan, start_date, end_date):
        self.user_id = user_id
        self.plan = plan
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self):
        return self.start_date <= datetime.now() <= self.end_date

    def update_subscription(self, new_plan, new_end_date):
        self.plan = new_plan
        self.end_date = new_end_date

class SubscriptionSchema(Schema):
    user_id = fields.Str(required=True)
    plan = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime(required=True)
```