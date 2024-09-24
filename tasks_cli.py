import typer
from rich.console import Console
from rich.table import Table
from sqlalchemy.sql import func
from models.todo import Todo
from models.database import session
from models.user import User

console = Console()
app = typer.Typer()

@app.command(short_help='adds an item')
def add(task: str, category: str):
    count = session.query(func.count(Todo.id)).scalar()
    todo = Todo(task=task, category=category)
    todo.position = count if count else 0
    session.add(todo)
    session.commit()
    typer.echo(f"adding {task}, {category}")
    show()

@app.command()
def delete(position: int):
    typer.echo(f"deleting {position}")
    todo = session.query(Todo).filter_by(position=position-1).first()
    if todo:
        session.delete(todo)
        session.commit()
        # indices in UI begin at 1, but in database at 0
        todos_to_change = session.query(Todo).filter(Todo.position > position-1).all()
        for t in todos_to_change:
            t.position -= 1
        session.commit()
    show()

@app.command()
def update(position: int, task: str = None, category: str = None):
    typer.echo(f"updating {position}")
    todo = session.query(Todo).filter_by(position=position-1).first()
    if todo:
        if task is not None:
            todo.task = task
        if category is not None:
            todo.category = category
        session.commit()
    show()

@app.command()
def complete(position: int):
    typer.echo(f"complete {position}")
    todo = session.query(Todo).filter_by(position=position-1).first()
    if todo:
        todo.status = 2
        session.commit()
    show()

@app.command()
def show():
    tasks = session.query(Todo).all()
    console.print("[bold magenta]Todos[/bold magenta]!", "💻")
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Todo", min_width=20)
    table.add_column("Category", min_width=12, justify="right")
    table.add_column("Done", min_width=12, justify="right")

    def get_category_color(category):
        COLORS = {'Learn': 'cyan', 'YouTube': 'red', 'Sports': 'cyan', 'Study': 'green'}
        if category in COLORS:
            return COLORS[category]
        return 'white'

    for idx, task in enumerate(tasks, start=1):
        c = get_category_color(task.category)
        is_done_str = '✅' if task.status == 2 else '❌'
        table.add_row(str(idx), task.task, f'[{c}]{task.category}[/{c}]', is_done_str)
    console.print(table)

@app.command()
def create_user(username: str):
    user = session.query(User).filter_by(username=username).first()
    if not user:
        user = User(username=username)
        session.add(user)  # Add the user to the session
        session.commit()
        typer.echo(f"User '{username}' created successfully!")
    else:
        typer.echo(f"User '{username}' already exists.")
    show()

@app.command()
def show_users():
    users = session.query(User).all()
    console.print("[bold green]Users[/bold green]!", "👩🏿‍💻")
    
    # Create a table with headers
    table = Table(show_header=True, header_style="bold blue")
    table.add_column("#", style="dim", width=6)
    table.add_column("Username", style="green")
    table.add_column("Todos", style="magenta")
    
    # Populate the table with user data
    for idx, user in enumerate(users, start=1):
        todos_list = [todo.task for todo in user.todos]  # Access todos through relationship
        todos_display = ", ".join(todos_list) if todos_list else "No todos"
        table.add_row(str(idx), user.username, todos_display)
    # Print the table to the console
    console.print(table)


@app.command()
def assign_task(username: str, task: str):
    # Query the user by username
    user = session.query(User).filter_by(username=username).first()
    
    if not user:
        console.print(f"[red]User '{username}' not found![/red]")
        raise typer.Exit()

    # Query the task or create it if it doesn't exist
    todo = session.query(Todo).filter_by(task=task).first()
    
    if not todo:
        console.print(f"[yellow]Task '{task}' not found, creating a new task.[/yellow]")
        todo = Todo(task=task, category="Sports")
        session.add(todo)
    
    # Assign the task to the user (link in the many-to-many relationship)
    user.todos.append(todo)
    
    # Commit the changes
    session.commit()
    
    console.print(f"[green]Task '{task}' has been assigned to user '{username}'![/green]")


# user creation:
# new_user = create_user("Joseph Michael")
# new_user2 = create_user("Mark Daniels")

# Create a connection in the customer_restaurants table
# new_user.todos.append('Prof')
# new_user2.todos.append('Beef')

if __name__ == "__main__":
    app()
