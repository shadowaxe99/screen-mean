```python
from marshmallow import Schema, fields

class Project:
    def __init__(self, title, description, screenplay, user_id):
        self.title = title
        self.description = description
        self.screenplay = screenplay
        self.user_id = user_id

    def update_project(self, title=None, description=None, screenplay=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if screenplay:
            self.screenplay = screenplay

    def get_project_details(self):
        return {
            "title": self.title,
            "description": self.description,
            "screenplay": self.screenplay,
            "user_id": self.user_id
        }

class ProjectSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    screenplay = fields.Str(required=True)
    user_id = fields.Int(required=True)
```