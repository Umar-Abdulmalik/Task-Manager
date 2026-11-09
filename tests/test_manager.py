import pytest

from src.manager import TaskManager


@pytest.fixture
def manager(tmp_path):
    return TaskManager(tmp_path / "tasks.json")


def test_add_assigns_incrementing_ids(manager):
    first = manager.add("Study Python")
    second = manager.add("Practice Git")
    assert (first.id, second.id) == (1, 2)


def test_complete_marks_task_done(manager):
    task = manager.add("Study")
    manager.complete(task.id)
    assert manager.list_tasks()[0].done is True


def test_delete_removes_task(manager):
    task = manager.add("Study")
    manager.delete(task.id)
    assert manager.list_tasks() == []


def test_unknown_id_raises_error(manager):
    with pytest.raises(ValueError):
        manager.complete(99)


def test_search_ignores_capital_letters(manager):
    manager.add("Study Python")
    manager.add("Buy bread")
    results = manager.search("python")
    assert [task.title for task in results] == ["Study Python"]


def test_tasks_survive_restart(tmp_path):
    path = tmp_path / "tasks.json"
    TaskManager(path).add("Remember me")
    reloaded = TaskManager(path)
    assert reloaded.list_tasks()[0].title == "Remember me"