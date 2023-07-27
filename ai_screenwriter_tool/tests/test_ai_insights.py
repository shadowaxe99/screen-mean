```python
import unittest
from ai_screenwriter_tool import ai_insights

class TestAIInsights(unittest.TestCase):

    def setUp(self):
        self.ai_insights = ai_insights.generateAIInsights()

    def test_generateAIInsights(self):
        self.assertIsNotNone(self.ai_insights, "Should not be None")

    def test_aiInsightsType(self):
        self.assertIsInstance(self.ai_insights, dict, "Should be a dictionary")

    def test_aiInsightsKeys(self):
        self.assertIn('plot_twists', self.ai_insights, "Should contain 'plot_twists' key")
        self.assertIn('character_development', self.ai_insights, "Should contain 'character_development' key")
        self.assertIn('dialogues', self.ai_insights, "Should contain 'dialogues' key")
        self.assertIn('story_arcs', self.ai_insights, "Should contain 'story_arcs' key")

if __name__ == '__main__':
    unittest.main()
```