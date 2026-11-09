import pytest
from src.task import Task


def test_new_task_is_not_done():
    assert Task(id=1, title="Study Python").done is False


def test_title_is_trimmed():
    assert Task(id=1, title="  Read  ").title == "Read"


def test_empty_title_raises_error():
    with pytest.raises(ValueError):
        Task(id=1, title="   ")


def test_round_trip_through_dict():
    task = Task(id=2, title="Practice")
    assert Task.from_dict(task.to_dict()) == task