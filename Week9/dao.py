from tasks import Task, RecurringTask, PriorityTask, TaskFactory
import datetime
from abc import ABC, abstractmethod
import csv

# Abstract base class for all Data Access Object (DAO) implementations
class TaskDAO(ABC):
    @abstractmethod
    def get_all_tasks(self) -> list[Task]:
        """Retrieve all tasks from the storage"""
        pass

    @abstractmethod
    def save_all_tasks(self, tasks: list[Task]) -> None:
        """Save all tasks to the storage"""
        pass

# Test DAO implementation that provides hardcoded tasks (used for testing)
class TaskTestDAO(TaskDAO):
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def get_all_tasks(self) -> list[Task]:
        """Returns a hardcoded list of tasks for testing"""
        task_list = [
            Task("Buy groceries", datetime.datetime.now() - datetime.timedelta(days=4)),
            Task("Do laundry", datetime.datetime.now() + datetime.timedelta(days=2)),
            Task("Clean room", datetime.datetime.now() - datetime.timedelta(days=1)),
            Task("Do homework", datetime.datetime.now() + datetime.timedelta(days=3)),
            Task("Walk dog", datetime.datetime.now() + datetime.timedelta(days=5)),
            Task("Do dishes", datetime.datetime.now() + datetime.timedelta(days=6))
        ]

        # Create a recurring task and add some completed dates
        r_task = RecurringTask("Go to the gym", datetime.datetime.now(), datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=7))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=14))
        r_task.completed_dates.append(datetime.datetime.now() - datetime.timedelta(days=22))
        r_task.date_created = datetime.datetime.now() - datetime.timedelta(days=28)

        task_list.append(r_task)

        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        """No-op for test DAO"""
        pass

# CSV DAO implementation for reading/writing tasks to a CSV file
class TaskCsvDAO(TaskDAO):
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path
        self.fieldnames = [
            "title", "type", "date_due", "completed",
            "interval", "completed_dates", "date_created", "priority"
        ]

    def get_all_tasks(self) -> list[Task]:
        """Reads all tasks from a CSV file and returns them as a list"""
        task_list: list[Task] = []

        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                # Extract common fields
                title = row["title"]
                task_type = row["type"]
                due_date = datetime.datetime.strptime(row["date_due"], "%Y-%m-%d")
                completed = row["completed"].lower() == "true"
                date_created = datetime.datetime.strptime(row["date_created"], "%Y-%m-%d")

                # Optional fields
                interval_str = row.get("interval", "")
                completed_dates_str = row.get("completed_dates", "")
                priority_str = row.get("priority", "")

                # Instantiate correct task type
                if task_type == "RecurringTask":
                    interval_days = int(interval_str.split(" ")[0]) if interval_str else 0
                    task = TaskFactory.create_task(title, due_date, interval=datetime.timedelta(days=interval_days))

                    # Add completed dates for recurring tasks
                    if isinstance(task, RecurringTask):
                        if completed_dates_str.strip():
                            raw_dates = [d.strip() for d in completed_dates_str.split(",") if d.strip()]
                            task.completed_dates = [
                                datetime.datetime.strptime(d, "%Y-%m-%d") for d in raw_dates
                            ]
                        else:
                            task.completed_dates = []

                elif task_type == "PriorityTask":
                    # Convert and validate priority (default to 1 if missing/invalid)
                    priority = int(priority_str) if priority_str.isdigit() else 1
                    task = TaskFactory.create_task(title, due_date, priority=priority)

                else:  # Standard Task
                    task = TaskFactory.create_task(title, due_date)

                # Set common properties for all task types
                task.completed = completed
                task.date_created = date_created

                task_list.append(task)

        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        """Saves all tasks to the CSV file"""
        with open(self.storage_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

            for task in tasks:
                row = {
                    "title": task.title,
                    "type": "Task",
                    "date_due": task.date_due.strftime("%Y-%m-%d"),
                    "completed": str(task.completed),
                    "interval": "",
                    "completed_dates": "",
                    "date_created": task.date_created.strftime("%Y-%m-%d"),
                    "priority": ""
                }

                # Handle saving additional data for RecurringTask
                if isinstance(task, RecurringTask):
                    row["type"] = "RecurringTask"
                    row["interval"] = str(task.interval)
                    row["completed_dates"] = ",".join([
                        date.strftime("%Y-%m-%d") for date in task.completed_dates
                    ])

                # Handle saving additional data for PriorityTask
                elif isinstance(task, PriorityTask):
                    row["type"] = "PriorityTask"
                    row["priority"] = str(task.priority)

                writer.writerow(row)
