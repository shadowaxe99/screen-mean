```python
from marshmallow import Schema, fields

class User:
    def __init__(self, id, name, email, subscription_status, tokens):
        self.id = id
        self.name = name
        self.email = email
        self.subscription_status = subscription_status
        self.tokens = tokens

    def update_subscription_status(self, status):
        self.subscription_status = status

    def update_tokens(self, tokens):
        self.tokens = tokens

class UserSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    subscription_status = fields.Str(required=True)
    tokens = fields.Int(required=True)
```