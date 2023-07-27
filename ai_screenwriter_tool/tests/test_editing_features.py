```python
import unittest
from ai_screenwriter_tool.editing_features import applyEditingFeatures

class TestEditingFeatures(unittest.TestCase):

    def setUp(self):
        self.sample_script = "INT. HOUSE - DAY\n\nA man, JOHN, is sitting on a chair."
        self.sample_character_sheet = {"name": "JOHN", "traits": ["brave", "smart"], "role": "protagonist"}

    def test_applyEditingFeatures(self):
        edited_script, edited_character_sheet = applyEditingFeatures(self.sample_script, self.sample_character_sheet)

        # Check if the function returns a tuple
        self.assertIsInstance(edited_script, str)
        self.assertIsInstance(edited_character_sheet, dict)

        # Check if the function modifies the script and character sheet
        self.assertNotEqual(edited_script, self.sample_script)
        self.assertNotEqual(edited_character_sheet, self.sample_character_sheet)

if __name__ == '__main__':
    unittest.main()
```