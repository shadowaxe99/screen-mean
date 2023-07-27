```python
import unittest
from ai_screenwriter_tool.database import Database
from ai_screenwriter_tool.user import User
from ai_screenwriter_tool.project import Project
from ai_screenwriter_tool.token import Token
from ai_screenwriter_tool.subscription import Subscription

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database()
        self.user = User("John Doe", "john.doe@example.com")
        self.project = Project("Project 1", self.user)
        self.token = Token(self.user)
        self.subscription = Subscription(self.user)

    def test_add_user(self):
        self.db.add_user(self.user)
        self.assertIn(self.user, self.db.users)

    def test_add_project(self):
        self.db.add_project(self.project)
        self.assertIn(self.project, self.db.projects)

    def test_add_token(self):
        self.db.add_token(self.token)
        self.assertIn(self.token, self.db.tokens)

    def test_add_subscription(self):
        self.db.add_subscription(self.subscription)
        self.assertIn(self.subscription, self.db.subscriptions)

    def test_remove_user(self):
        self.db.add_user(self.user)
        self.db.remove_user(self.user)
        self.assertNotIn(self.user, self.db.users)

    def test_remove_project(self):
        self.db.add_project(self.project)
        self.db.remove_project(self.project)
        self.assertNotIn(self.project, self.db.projects)

    def test_remove_token(self):
        self.db.add_token(self.token)
        self.db.remove_token(self.token)
        self.assertNotIn(self.token, self.db.tokens)

    def test_remove_subscription(self):
        self.db.add_subscription(self.subscription)
        self.db.remove_subscription(self.subscription)
        self.assertNotIn(self.subscription, self.db.subscriptions)

if __name__ == '__main__':
    unittest.main()
```