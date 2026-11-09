import json
from pathlib import Path

from src.task import Task


class TaskManager:
    """Keeps a list of tasks and saves them to a JSON file."""

    def __init__(self, filepath="tasks.json"):
        self.filepath = Path(filepath)
        self.tasks = []
        self.load()

    def load(self):
        if not self.filepath.exists():
            self.tasks = []
            return
        try:
            text = self.filepath.read_text(encoding="utf-8")
            self.tasks = [Task.from_dict(item) for item in json.loads(text)]
        except (json.JSONDecodeError, TypeError, ValueError) as error:
            raise ValueError(f"Could not read {self.filepath}: {error}")

    def save(self):
        data = [task.to_dict() for task in self.tasks]
        self.filepath.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def _find(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"No task with ID {task_id}.")

    def add(self, title):
        next_id = max((task.id for task in self.tasks), default=0) + 1
        task = Task(id=next_id, title=title)
        self.tasks.append(task)
        self.save()
        return task

    def list_tasks(self):
        return list(self.tasks)

    def complete(self, task_id):
        task = self._find(task_id)
        task.done = True
        self.save()
        return task

    def delete(self, task_id):
        task = self._find(task_id)
        self.tasks.remove(task)
        self.save()

    def search(self, keyword):
        keyword = keyword.lower()
        return [task for task in self.tasks if keyword in task.title.lower()]