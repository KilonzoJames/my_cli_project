import pytest
from models.todo import Todo

def test_creates_todo_instance():
    mylist = Todo('todo', 'Personal')
    mylist.add("task")
    assert mylist.size() == 1
def test_if_todo_exists():
    mylist = Todo('todo', 'Personal')
    mylist.add("task")
    assert "task" in mylist.get_todos() 
def test_check_when_todolist_full():
    mylist = Todo('todo', 'Personal', max_size=10)
    for _ in range(10):
        mylist.add('todo')

    with pytest.raises(OverflowError):
        mylist.add('todo')
