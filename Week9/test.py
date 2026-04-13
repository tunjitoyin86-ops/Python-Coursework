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


from tasks import Task, RecurringTask, PriorityTask, TaskFactory
import datetime
from abc import ABC, abstractmethod
import csv

class TaskDAO(ABC):
    @abstractmethod
    def get_all_tasks(self) -> list[Task]:
        pass

    @abstractmethod
    def save_all_tasks(self, tasks: list[Task]) -> None:
        pass

class TaskTestDAO(TaskDAO):
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def get_all_tasks(self) -> list[Task]:
        task_list =[
            Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)),
            Task("Do laundry", datetime.datetime.now() - datetime.timedelta(days=-2)),
            Task("Clean room", datetime.datetime.now() + datetime.timedelta(days=-1)),
            Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)),
            Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)),
            Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))
        ]

        # sample recurring task
        r_task = RecurringTask("Go to the gym", datetime.datetime.now(), datetime.timedelta(days=7))
        # propagate the recurring task with some completed dates
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)

        task_list.append(r_task)

        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        pass


class TaskCsvDAO(TaskDAO):
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

        self.fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created", "priority"]

    def get_all_tasks(self) -> list[Task]:
        task_list : list[Task]= []
        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                task_type = row["type"]
                task_title = row["title"]
                task_date_due = row["date_due"]
                task_completed = row["completed"]
                task_interval = row["interval"]
                task_date_created = row["date_created"]
                task_completed_dates = row["completed_dates"]
                priority_str = row.get("priority", "")

                task: Task | RecurringTask # declare the type of task as Task or RecurringTask for the type checker
                
                if task_type == "RecurringTask":
                    interval_days = int(task_interval.split(" ")[0]) if task_interval else 0
                    task = TaskFactory.create_task(
                        task_title,
                        datetime.datetime.strptime(task_date_due, "%Y-%m-%d"),
                        interval=datetime.timedelta(days=interval_days)
                    )
                    if isinstance(task, RecurringTask):
                        if task_completed_dates and task_completed_dates.strip():
                            raw_dates = [d.strip() for d in task_completed_dates.split(",") if d.strip()]
                            task.completed_dates = [datetime.datetime.strptime(d, "%Y-%m-%d") for d in raw_dates]
                        else:
                            task.completed_dates = []

                elif task_type == "PriorityTask":
                    priority_value = int(priority_str) if priority_str.isdigit() else 1
                    task = TaskFactory.create_task(
                        task_title,
                        datetime.datetime.strptime(task_date_due, "%Y-%m-%d"),
                        priority=priority_value
                    )
                    
                else:
                    task = TaskFactory.create_task(
                        task_title,
                        datetime.datetime.strptime(task_date_due, "%Y-%m-%d")
                    )

                task.date_created = datetime.datetime.strptime(task_date_created, "%Y-%m-%d")
                task.completed = True if task_completed.lower() == "true" else False
                
                task_list.append(task)
        return task_list



    def save_all_tasks(self, tasks: list[Task]) -> None:
        with open(self.storage_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            for task in tasks:
                row = {}


                row["title"] = task.title
                row["type"] = "RecurringTask" if isinstance(task, RecurringTask) else "Task"
                row["date_due"] = task.date_due.strftime("%Y-%m-%d")
                row["completed"] = str(task.completed)
                row["interval"]  = str(task.interval) if isinstance(task, RecurringTask) else ""
                row["completed_dates"] = ",".join([date.strftime("%Y-%m-%d") for date in task.completed_dates]) if isinstance(task, RecurringTask) else ""
                row["date_created"] = task.date_created.strftime("%Y-%m-%d")
                row["priority"] = str(task.priority) if isinstance(task, PriorityTask) else ""
                writer.writerow(row)