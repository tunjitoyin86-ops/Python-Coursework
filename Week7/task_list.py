# Import necessary modules
import time        # used to pause the program for a short time
import sys         # used to exit the program
import datetime    # used to handle dates and times
from tasks import Task       # import the Task class from tasks.py
from users import Owner  # import Owner class from users.py

class TaskList:
    """Represents a user's list of tasks."""

    def __init__(self, owner: Owner) -> None:
        """
        Creates a task list for a specific user.
        The owner's name is saved and the task list starts empty.
        """
        self.owner = owner
        self.tasks: list[Task] = []      # list to store task objects

    def add_task(self, title: str, description: str, due_date: datetime.datetime) -> None:
        """
        Adds a new task to the list.
        """
        task = Task(title, due_date, description)
        self.tasks.append(task)
        print(f"Task '{task.title}' added successfully on {task.date_created.strftime('%Y-%m-%d %H:%M')}.")
        
    def add_task_object(self, task: Task) -> None:
        """Adds an already created task object (either Task or RecurringTask) to the list."""
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
        Displays only the uncompleted tasks from the task list.
        Shows a message if there are no uncompleted tasks.
        """
        if not self.uncompleted_tasks:
            print("No uncompleted tasks found.")
        else:
            print("The following tasks are still to be done:")
            for task in self.uncompleted_tasks:
                ix = self.tasks.index(task)  # Get original index in full list
                print(f"{ix}: {task}")       # Show index and task info
            print(f"Uncompleted Tasks: {len(self.uncompleted_tasks)}")


    def mark_completed(self) -> None:
        """
        Lets the user mark a task as done using controlled access.
        """
        self.view_tasks()
        try:
            index = int(input("Enter task number to mark complete: ")) - 1
            task = self.get_task(index)  # uses encapsulated method
            task.mark_completed()
        except (ValueError, IndexError):
            print("Invalid task number.")

    @property
    def uncompleted_tasks(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]

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

    def change_due_date(self) -> None:
        """
        Allows the user to change the due date of a task.
        """
        self.view_tasks()
        try:
            index = int(input("Enter task number to change due date: ")) - 1
            if 0 <= index < len(self.tasks):
                new_due_date = datetime.datetime.strptime(input("New due date (YYYY-MM-DD): "), "%Y-%m-%d")
                self.tasks[index].due_date = new_due_date
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
        overdue = [task for task in self.tasks if task.due_date < today and not task.completed]
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

    def get_task(self, index: int) -> Task:
        """
        Returns the task at the given index if it's valid.

        Args:
            index (int): The index of the task to retrieve.

        Returns:
            Task: The task at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if 0 <= index < len(self.tasks):
            return self.tasks[index]
        else:
            raise IndexError("Task index is out of range.")
        

