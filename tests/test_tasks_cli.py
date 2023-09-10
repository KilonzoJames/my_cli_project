import typer
from typer.testing import CliRunner
from tasks_cli import app

runner = CliRunner()

def test_add_command():
    result = runner.invoke(app, ["add", "Task 1", "Personal"])
    assert result.exit_code == 0
    assert "adding Task 1, Personal" in result.output

def test_show_command():
    result = runner.invoke(app, ["show"])
    assert result.exit_code == 0
    assert "Todos" in result.output

def test_delete_command():
    runner.invoke(app, ["add", "Task to delete", "Personal"])  # Add a task first
    result = runner.invoke(app, ["delete", "1"])
    assert result.exit_code == 0
    assert "deleting 1" in result.output

# def test_update_command():
#     runner.invoke(app, ["add", "Task to update", "Personal"])  # Add a task first
#     result = runner.invoke(app, ["update", "1", "Updated Task", "Work"])
#     assert result.exit_code == 0
#     assert "updating 1" in result.output

def test_complete_command():
    runner.invoke(app, ["add", "Task to complete", "Personal"])  # Add a task first
    result = runner.invoke(app, ["complete", "1"])
    assert result.exit_code == 0
    assert "complete 1" in result.output

# def test_create_user_command():
#     result = runner.invoke(app, ["create_user", "John Doe"])
#     assert result.exit_code == 0
#     assert "Joseph Michael" in result.output  # Check for a sample username

# Add more tests as needed for your specific use cases
