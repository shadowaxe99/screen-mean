```python
import unittest
from ai_screenwriter_tool.token import Token

class TestToken(unittest.TestCase):

    def setUp(self):
        self.token = Token()

    def test_token_initialization(self):
        self.assertEqual(self.token.count, 0, "Initial token count should be 0")

    def test_add_token(self):
        self.token.add_token(5)
        self.assertEqual(self.token.count, 5, "Token count should be 5 after adding 5 tokens")

    def test_use_token(self):
        self.token.add_token(5)
        self.token.use_token(3)
        self.assertEqual(self.token.count, 2, "Token count should be 2 after using 3 tokens")

    def test_use_token_insufficient(self):
        self.token.add_token(2)
        with self.assertRaises(ValueError):
            self.token.use_token(3)

    def test_reset_token(self):
        self.token.add_token(5)
        self.token.reset_token()
        self.assertEqual(self.token.count, 0, "Token count should be 0 after reset")

if __name__ == '__main__':
    unittest.main()
```