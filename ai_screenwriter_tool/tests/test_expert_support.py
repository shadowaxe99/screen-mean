```python
import unittest
from ai_screenwriter_tool.expert_support import seekExpertSupport

class TestExpertSupport(unittest.TestCase):

    def setUp(self):
        self.user = {
            "name": "Test User",
            "email": "testuser@example.com",
            "subscription": "premium"
        }
        self.project = {
            "title": "Test Project",
            "genre": "Drama",
            "script": "INT. TEST LOCATION - DAY\n\nTest character enters..."
        }

    def test_seekExpertSupport(self):
        response = seekExpertSupport(self.user, self.project)
        self.assertIsInstance(response, dict)
        self.assertIn('feedback', response)
        self.assertIn('guidance', response)

if __name__ == '__main__':
    unittest.main()
```