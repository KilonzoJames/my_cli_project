# Task Manager CLI

## Overview

The Task Manager CLI is a command-line tool that helps you manage your tasks and to-do lists efficiently. It provides a simple and convenient way to add, delete, update, complete, and view tasks right from your terminal.

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Database](#database)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started with the Task Manager CLI, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/KilonzoJames/my_cli_project.git
   cd my_cli_project
2. Create a virtual environment (optional but recommended):
pipenv install
pipenv shell
pytest

3. Initialize the database:

4. Install dependencies:
pip install -r requirements.txt

## Usage
The Task Manager CLI provides several commands to manage your tasks:
For help use:
- python3 tasks_cli.py --help
- python3 tasks_cli.py show --help
- python3 tasks_cli.py add --help
- python3 tasks_cli.py update --help
- python3 tasks_cli.py delete --help

1. python3 tasks_cli.py add "arg" "arg": Add a new task.
2. python3 tasks_cli.py delete (arg): Delete a task by specifying its position.
3. python3 tasks_cli.py update [POSITION] --task "NEW_TASK_TEXT" --category "NEW_CATEGORY_TEXT": Update a task's details (task name or category).
4. python3 tasks_cli.py complete [POSITION]: Mark a task as completed.
5. python3 tasks_cli.py show: Display the list of tasks.

## Features
Add Tasks: Quickly add new tasks with a name and an optional category.

Delete Tasks: Remove tasks by specifying their position in the list.

Update Tasks: Modify task details, including the task name and category.

Complete Tasks: Mark tasks as completed, making it easy to track your progress.

List Tasks: View all your tasks with an informative table that includes task status and category.

## Dependencies
This project relies on the following Python packages, which are automatically installed when you follow the installation instructions:

rich: A library for adding color and style to terminal output.
typer: A Python library for building command-line applications.
pytest: A testing framework for Python that simplifies the process of writing and executing test cases for your Python code.

## Database
The Task Manager CLI uses an SQLite database to store task data. The database schema is managed using Alembic for easy updates and migrations. You can find the database file at my_database.db.

## Contributing
We welcome contributions to the Task Manager CLI! If you want to improve the project, fix a bug, or add a new feature, please follow these steps:

- Fork the repository.
- Create a new branch with a descriptive name:
- Make your changes and commit them:
- Push your changes to your forked repository:
- Create a Pull Request on the original repository.

## License
This project is licensed under the MIT License.