```python
from datetime import datetime
from marshmallow import Schema, fields, post_load

class Token:
    def __init__(self, id, user_id, value, expiry_date):
        self.id = id
        self.user_id = user_id
        self.value = value
        self.expiry_date = expiry_date

    def is_valid(self):
        return datetime.now() < self.expiry_date

class TokenSchema(Schema):
    id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    value = fields.Float(required=True)
    expiry_date = fields.DateTime(required=True)

    @post_load
    def make_token(self, data, **kwargs):
        return Token(**data)
```