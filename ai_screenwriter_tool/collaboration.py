```python
from .user import User
from .project import Project

class Collaboration:
    def __init__(self):
        self.active_users = []
        self.active_projects = []

    def enableCollaboration(self, user: User, project: Project):
        if user not in self.active_users:
            self.active_users.append(user)
        if project not in self.active_projects:
            self.active_projects.append(project)

    def realTimeFeedback(self, user: User, feedback: str):
        if user in self.active_users:
            return f"Real-time feedback from {user.name}: {feedback}"
        else:
            return "User is not currently collaborating on a project."

    def realTimeEditing(self, user: User, project: Project, edits: str):
        if user in self.active_users and project in self.active_projects:
            project.applyEdits(edits)
            return f"Real-time edits applied by {user.name} to {project.title}."
        else:
            return "User is not currently collaborating on this project."
```