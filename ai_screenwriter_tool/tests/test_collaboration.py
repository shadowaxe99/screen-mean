```python
import unittest
from ai_screenwriter_tool.collaboration import enableCollaboration

class TestCollaboration(unittest.TestCase):

    def setUp(self):
        self.user1 = {"username": "user1", "email": "user1@example.com"}
        self.user2 = {"username": "user2", "email": "user2@example.com"}
        self.project = {"title": "Test Project", "description": "This is a test project"}

    def test_enableCollaboration(self):
        result = enableCollaboration(self.user1, self.user2, self.project)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```