from controllers import TaskManagerController
from tasks import TaskFactory
import datetime

class CommandLineUI:
    def _print_menu(self) -> None:
        print("\nTo-Do List Manager") 
        print("1. Add a task") 
        print("2. View tasks") 
        print("3. Select a task")
        print("4. Import tasks")
        print("5. Export tasks")
        print("q. Quit")

    def run(self) -> None:
        name = input("Enter your name: ").strip().capitalize()
        self.controller = TaskManagerController(name)
        print(f"\nWelcome, {name}! Let's manage your tasks.")

        load_default = input("Would you like to load your default task list (tasks.csv)? (y/n): ").lower()
        if load_default == "y":
            try:
                self.controller.load_tasks("tasks.csv")
                print("Default tasks loaded successfully.")
            except FileNotFoundError:
                print("Default task file not found.")

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
        title = input("Enter a task title: ").strip()
        input_date = input("Enter due date (YYYY-MM-DD): ")
        try:
            due_date = datetime.datetime.strptime(input_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format.")
            return

        while True:
            recurring = input("Is this a recurring task? (y/n): ").lower()
            if recurring == "y":
                interval_days = int(input("Enter interval in days: "))
                task = TaskFactory.create_task(title, due_date, interval=datetime.timedelta(days=interval_days))
                break
            elif recurring == "n":
                task = TaskFactory.create_task(title, due_date)
                break
            else:
                print("Please enter 'y' or 'n'.")

        self.controller.add_task(task)
        print("Task added successfully.")

    def _view_tasks(self):
        tasks = self.controller.get_all_tasks()
        if not tasks:
            print("No tasks available.")
            return
        for ix, task in tasks:
            print(f"{ix}: {task}")

    def _select_task(self):
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
        path = input("Enter the CSV file path: ")
        try:
            self.controller.load_tasks(path)
            print("Tasks imported Successfully.")
        except FileNotFoundError:
            print("File not found. Please check the path and try again.")

    def _export_tasks(self):
        path = input("Enter path to save CSV file: ")
        try:
            self.controller.save_tasks(path)
            print("Tasks saved.")
        except Exception as e:
            print(f"Error saving file: {e}")





