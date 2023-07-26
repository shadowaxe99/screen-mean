```python
from ai_screenwriter_tool.user import User
from ai_screenwriter_tool.project import Project

class ExpertSupport:
    def __init__(self):
        self.experts = self.load_experts()

    def load_experts(self):
        # This function should load the list of experts from a database or a file
        # For simplicity, we will return a static list
        return ["Expert1", "Expert2", "Expert3"]

    def seekExpertSupport(self, user: User, project: Project):
        # This function should connect the user with an expert for personalized feedback and guidance
        # For simplicity, we will print a message
        print(f"Connecting {user.name} with an expert for project {project.title}...")

    def provideFeedback(self, user: User, project: Project, feedback: str):
        # This function should allow the expert to provide feedback on the user's project
        # For simplicity, we will print a message
        print(f"Expert provided the following feedback for {user.name}'s project {project.title}: {feedback}")

    def guideUser(self, user: User, guidance: str):
        # This function should allow the expert to provide guidance to the user
        # For simplicity, we will print a message
        print(f"Expert provided the following guidance to {user.name}: {guidance}")
```