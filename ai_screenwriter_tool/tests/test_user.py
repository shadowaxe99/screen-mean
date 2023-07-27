```python
import unittest
from ai_screenwriter_tool.user import User, UserSchema

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User("John Doe", "john.doe@example.com", "password123")
        self.user_schema = UserSchema()

    def test_user_creation(self):
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertEqual(self.user.password, "password123")

    def test_user_schema(self):
        user_data = self.user_schema.dump(self.user)
        expected_data = {
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "password123"
        }
        self.assertEqual(user_data, expected_data)

    def test_update_user(self):
        self.user.updateUser("Jane Doe", "jane.doe@example.com", "password456")
        self.assertEqual(self.user.name, "Jane Doe")
        self.assertEqual(self.user.email, "jane.doe@example.com")
        self.assertEqual(self.user.password, "password456")

if __name__ == "__main__":
    unittest.main()
```