from controllers import TaskManagerController
from tasks import TaskFactory
import datetime

class CommandLineUI:
    """
    Command-line user interface for the To-Do List Manager.
    Handles user interaction, input/output, and delegates actions to the controller.
    """

    def _print_menu(self) -> None:
        """Display the main menu options."""
        print("\nTo-Do List Manager") 
        print("1. Add a task") 
        print("2. View tasks") 
        print("3. Select a task")
        print("4. Import tasks")
        print("5. Export tasks")
        print("q. Quit")

    def run(self) -> None:
        """
        Main loop to run the to-do list application.
        Prompts user for their name and presents menu options for task management.
        """
        name = input("Enter your name: ").strip().capitalize()
        self.controller = TaskManagerController(name)  # Initialize controller with user's name
        print(f"\nWelcome, {name}! Let's manage your tasks.")

        # Ask if the user wants to load the default task list
        load_default = input("Would you like to load your default task list (tasks.csv)? (y/n): ").lower()
        if load_default == "y":
            try:
                self.controller.load_tasks("tasks.csv")
                print("Default tasks loaded successfully.")
            except FileNotFoundError:
                print("Default task file not found.")

        # Menu loop
        while True:
            self._print_menu()
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self._add_task()
            elif choice == "2":
                self._view_tasks()
            elif choice == "3":
                self._select_task()
            elif choice == "4":
                self._import_tasks()
            elif choice == "5":
                self._export_tasks()
            elif choice == "q":
                print("Goodbye!")
                break
            else:
                print("Invalid choice.")

    def _add_task(self):
        """Prompt the user to create a new task and add it using the controller."""
        title = input("Enter a task title: ").strip()
        input_date = input("Enter due date (YYYY-MM-DD): ")

        try:
            due_date = datetime.datetime.strptime(input_date, "%Y-%m-%d")  # Parse due date
        except ValueError:
            print("Invalid date format.")
            return

        # Prompt for task type: standard, recurring, or priority
        while True:
            task_type = input("Is this (s)tandard, (r)ecurring or (p)riority task? (s/r/p): ").lower()
            if task_type == "r":
                interval_days = int(input("Enter interval in days: "))
                task = TaskFactory.create_task(title, due_date, interval=datetime.timedelta(days=interval_days))
                break
            elif task_type == "p":
                try:
                    priority = int(input("Enter priority (1: low, 2: medium, 3: high): "))
                    task = TaskFactory.create_task(title, due_date, priority=priority)
                    break
                except ValueError:
                    print("Invalid priority number.")
            elif task_type == "s":
                task = TaskFactory.create_task(title, due_date)
                break
            else:
                print("Please enter 's', 'r' or 'p'.")

        self.controller.add_task(task)  # Add task to controller
        print("Task added successfully.")

    def _view_tasks(self):
        """Display all current tasks to the user."""
        tasks = self.controller.get_all_tasks()
        if not tasks:
            print("No tasks available.")
            return
        for ix, task in tasks:
            print(f"{ix}: {task}")

    def _select_task(self):
        """Allow the user to select a task for further actions like editing or completing."""
        try:
            ix = int(input("Enter task index: "))
            if self.controller.task_list.check_task_index(ix):
                print(f"Selected: {self.controller.task_list.get_task(ix)}")
            else:
                print("Invalid index.")
                return
        except ValueError:
            print("Please enter a valid number.")
            return

        # Task action menu
        while True:
            print("\n1. Remove task")
            print("2. Edit task")
            print("3. Mark as complete")
            print("q. Back to main menu")
            choice = input("Choice: ")

            if choice == "1":
                self.controller.remove_task(ix)
                print("Task removed.")
                break
            elif choice == "2":
                self._edit_task(ix)
                break
            elif choice == "3":
                self.controller.complete_task(ix)
                print("Task marked as completed.")
                break
            elif choice == "q":
                break
            else:
                print("Invalid choice.")

    def _edit_task(self, ix: int):
        """Edit selected task's title or due date."""
        print("1. Change title")
        print("2. Change due date")
        choice = input("Your choice: ")

        if choice == "1":
            new_title = input("Enter new title: ")
            self.controller.task_list.get_task(ix).change_title(new_title)
            print("Title updated.")
        elif choice == "2":
            try:
                new_date = input("Enter new due date (YYYY-MM-DD): ")
                date_obj = datetime.datetime.strptime(new_date, "%Y-%m-%d")
                self.controller.task_list.get_task(ix).change_date_due(date_obj)
                print("Due date updated.")
            except ValueError:
                print("Invalid date format.")
        else:
            print("Invalid choice.")

    def _import_tasks(self):
        """Import tasks from a CSV file."""
        path = input("Enter the CSV file path: ")
        try:
            self.controller.load_tasks(path)
            print("Tasks imported successfully.")
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")

    def _export_tasks(self):
        """Export current tasks to a CSV file."""
        path = input("Enter path to save CSV file: ")
        try:
            self.controller.save_tasks(path)
            print("Tasks saved.")
        except Exception as e:
            print(f"Error saving file: {e}")
