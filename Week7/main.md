# WEEK 4 
## Classes and Objects

This section dives into one of Python’s most powerful ideas — **object-oriented programming (OOP)**. Instead of just working with basic types like numbers and strings, OOP lets us build custom structures called **classes** that group related data and actions together. Think of a class as a recipe, and each object created from it as a dish made using that recipe.

Here, we focused on how to define our own **classes**, create **objects** from them, and use **methods** to give those objects useful behavior. We also learned how to keep our code clean and organized by splitting it into separate files (modules) and how to write clear explanations using docstrings and comments. These steps not only make the code easier to understand but also prepare it for future growth and collaboration.

## Section 1 Python Classes
### Exercise 1: Creating Classes and Initialising objects

In this exercise, we created two classes: **TaskList** and **Task**.

The **TaskList** class is like a manager that keeps track of multiple tasks. It has:

- an owner (the name of the user),

- a list called tasks that stores all task items.

- It also comes with some useful methods:

- <span style="color: blue;">**add_task()** – to add a new task,</span>

- <span style="color: blue;">**remove_task()** – to delete a task by its position,</span>

- <span style="color: blue;">**view_tasks()**</span> – to show all tasks,

- <span style="color: blue;">**list_options()**</span> – to display menu choices and handle user input.

Each individual task is created using the Task class. At this stage, the Task class simply holds the task's name/title.

All class properties (called instance variables) like owner and tasks are set inside a special method called __init__, which runs automatically when a new object is created.

This structure helps us keep our code clean, reusable, and easier to work with as we build more features later.

``` python
class TaskList:
        def __init__(self, owner: str) -> None:
            self.owner = owner.capitalize()  # capitalizes the user's name but just the first letter
            self.tasks: list[Task] = []      # list to store task objects

```
After setting up the __init__ method, the TaskList class is now ready to hold data. It can store the owner's name and a list of tasks. 
This setup prepares the class to be used in real examples where objects (task lists) can be created for different users

After creating a class, we can create actual objects from it. For example:

```python
my_task_list = TaskList("John")
print(my_task_list.owner)
```
















This project is about creating a simple **To-Do List** application using **Python**. The purpose is to help users keep track of their daily tasks by allowing them to add new tasks, view existing ones, mark tasks as completed, change task details, and remove tasks they no longer need. The program also keeps track of important information like when tasks are due and whether they have been finished.

To make the program easy to manage and understand, the code is divided into separate files, **main.py**, **tasks.py** and **task_list.py**, each handling a specific part of the application:

---

In the project:

* **tasks.py** contains the Task class, which handles individual tasks like title, description, due date, and completion status.
* **task\_list.py** contains the TaskList class, which manages a collection of Task objects and provides features like adding, removing, and marking tasks complete.
* **main.py** is the entry point where the user interacts with the program, using the features from the other modules.

## **main.py**


```python
import datetime
from task_list import TaskList
from tasks import Task

def main() -> None:
    """Runs the main program loop."""
    
    # Ask the user for their name and greet them
    name = input("Enter your name: ")
    print(f"Welcome {name.upper()}!")
    
    # Create a new TaskList for the user
    task_list = TaskList(name)

    # Start an infinite loop to show the menu until user chooses to exit
    while True:
        # Display the menu options
        print("\n To-Do List Menu")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task Completed")
        print("5. Change Task Title")
        print("6. Change Task Description")
        print("7. View Overdue Tasks")
        print("8. Exit")

        # Get user choice
        choice = input("Choose an option (1-8): ")

        # Handle each menu option
        if choice == "1":
            # Add a new task
            title = input("Task title: ")
            desc = input("Task description: ")
            due_str = input("Due date (YYYY-MM-DD): ")
            try:
                # Convert the due date string to a datetime object
                due = datetime.datetime.strptime(due_str, "%Y-%m-%d")
                # Create and add the new task to the list
                task_list.add_task(Task(title, due, desc))
            except ValueError:
                # If the date format is wrong, inform the user
                print("Invalid date format.")
        elif choice == "2":
            # Show all tasks
            task_list.view_tasks()
        elif choice == "3":
            # Remove a task by number
            try:
                ix = int(input("Enter task number to remove: ")) - 1
                task_list.remove_task(ix)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            # Mark a task as completed
            task_list.mark_completed()
        elif choice == "5":
            # Change the title of a task
            task_list.change_title()
        elif choice == "6":
            # Change the description of a task
            task_list.change_description()
        elif choice == "7":
            # View overdue tasks
            task_list.view_overdue_tasks()
        elif choice == "8":
            # Confirm and exit the program
            task_list.confirm_exit()
        else:
            # Handle invalid menu choices
            print("Invalid option. Please try again.")

# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()
```

## **task_list.py**

``` python
# Import necessary modules
import time        # used to pause the program for a short time
import sys         # used to exit the program
import datetime    # used to handle dates and times
from tasks import Task       # import the Task class from tasks.py

class TaskList:
    """Represents a user's list of tasks."""

    def __init__(self, owner: str) -> None:
        """
        Creates a task list for a specific user.
        The owner's name is saved and the task list starts empty.
        """
        self.owner = owner.capitalize()  # capitalizes the user's name
        self.tasks: list[Task] = []      # list to store task objects

    def add_task(self, task: Task) -> None:
        """
        Adds a new task to the list.
        The task must be created before adding.
        """
        self.tasks.append(task)
        print(f"Task '{task.title}' added successfully on {task.date_created.strftime('%Y-%m-%d %H:%M')}.")

    def remove_task(self, ix: int) -> None:
        """
        Removes a task from the list using its number.
        User must confirm the removal before it's deleted.
        """
        if 0 <= ix < len(self.tasks):
            confirm = input("Are you sure you want to delete this task? (yes/no): ")
            if confirm.lower() == 'yes':
                removed = self.tasks.pop(ix)
                print(f"Removed task: '{removed.title}'.")
            else:
                print("Task deletion cancelled.")
        else:
            print("Invalid index.")  # index is out of range

    def view_tasks(self) -> None:
        """
        Shows all tasks in the list.
        If there are no tasks, it lets the user know.
        """
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):  # numbers start at 1
                print(f"{i}. {task}")  # show task number and details

    def mark_completed(self) -> None:
        """
        Lets the user mark a task as done.
        The task is updated with the current date as completed date.
        """
        self.view_tasks()
        try:
            index = int(input("Enter task number to mark complete: ")) - 1
            if 0 <= index < len(self.tasks):
                self.tasks[index].mark_completed()
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")  # user didn't enter a number

    def change_title(self) -> None:
        """
        Allows the user to change the title of a task.
        """
        self.view_tasks()
        try:
            index = int(input("Enter task number to change title: ")) - 1
            if 0 <= index < len(self.tasks):
                new_title = input("New title: ")
                self.tasks[index].change_title(new_title)
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")

    def change_description(self) -> None:
        """
        Allows the user to change the description of a task.
        """
        self.view_tasks()
        try:
            index = int(input("Enter task number to change description: ")) - 1
            if 0 <= index < len(self.tasks):
                new_desc = input("New description: ")
                self.tasks[index].change_description(new_desc)
            else:
                print("Invalid number.")
        except ValueError:
            print("Invalid input.")

    def view_overdue_tasks(self) -> None:
        """
        Shows tasks that are past their due date and not yet completed.
        """
        today = datetime.datetime.now()
        overdue = [task for task in self.tasks if task.date_due < today and not task.completed]
        if overdue:
            print("Overdue tasks:")
            for task in overdue:
                print(task)
        else:
            print("No overdue tasks.")

    def confirm_exit(self) -> None:
        """
        Asks the user if they really want to exit the program.
        Exits if the user says yes, otherwise continues.
        """
        confirm = input("Are you sure you want to quit? (yes/no): ")
        if confirm.lower() == "yes":
            print("Exiting...")
            time.sleep(1)
            sys.exit()  # completely stops the program
        else:
            print("Exit cancelled.")

```

## **tasks.py**

```python
# Import the datetime module to work with dates and times
import datetime

class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, date_due: datetime.datetime, description: str = "") -> None:
        """
        Creates a new task with a title, due date, and optional description.

        Args:
            title (str): What the task is about.
            date_due (datetime): When the task should be finished.
            description (str): A short explanation about the task (optional).
        """
        self.title = title  # the name or title of the task
        self.completed = False  # task is not done yet
        self.date_created = datetime.datetime.now()  # time the task was created
        self.date_due = date_due  # when the task is due
        self.date_completed = datetime.datetime(1900, 1, 1)  # default value meaning "not yet completed"
        self.description = description  # optional description of the task

    def __str__(self) -> str:
        """
        Returns a readable summary of the task.

        Shows if the task is completed, when it was created and due, and its description.
        """
        status = "Yes" if self.completed else "No"  # show 'Yes' if completed
        # Show completed date only if task has been marked as done
        completed_info = (
            f", Completed on: {self.date_completed.strftime('%Y-%m-%d %H:%M')}"
            if self.date_completed != datetime.datetime(1900, 1, 1) else ""
        )
        return (
            f"Task: {self.title} | Completed: {status}{completed_info} | "
            f"Created on: {self.date_created.strftime('%Y-%m-%d')} | "
            f"Due: {self.date_due.strftime('%Y-%m-%d')} | "
            f"Description: {self.description}"
        )

    def mark_completed(self) -> None:
        """
        Marks the task as completed.

        This also saves the exact date and time the task was marked as done.
        """
        self.completed = True
        self.date_completed = datetime.datetime.now()  # set the time it was completed
        print(f"Task '{self.title}' marked as completed on {self.date_completed.strftime('%Y-%m-%d %H:%M')}.")

    def change_title(self, new_title: str) -> None:
        """
        Updates the task's title.

        Args:
            new_title (str): The new title the user wants to use.
        """
        old = self.title
        self.title = new_title
        print(f"Changed title from '{old}' to '{new_title}'.")

    def change_description(self, new_description: str) -> None:
        """
        Updates the task's description.

        Args:
            new_description (str): The new description the user wants to use.
        """
        old = self.description
        self.description = new_description
        print(f"Changed description from '{old}' to '{new_description}'.")
```

## **Conclusion**
This project shows how to build a basic **To-Do List app** using **Python** and **Object-Oriented Programming**. By separating the code into different files, it becomes easier to read, manage, and improve in the future.

Even though we can’t show the output here, the code includes clear comments and follows good practices like using type hints and modular design. The app lets users `add`, `view`, `edit`, and `complete tasks` easily through the terminal.