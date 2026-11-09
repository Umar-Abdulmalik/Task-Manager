from src.cli import format_task
from src.task import Task


def test_format_open_task():
    assert format_task(Task(id=1, title="Study")) == "[ ] 1. Study"


def test_format_done_task():
    assert format_task(Task(id=2, title="Read", done=True)) == "[x] 2. Read"