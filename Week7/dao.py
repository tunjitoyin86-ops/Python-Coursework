from tasks import Task, RecurringTask
import csv
from datetime import datetime, timedelta
import pickle


class TaskCsvDAO:
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path
        self.fieldnames = ["title", "type", "date_due", "completed", "interval", "completed_dates", "date_created"]

    def get_all_tasks(self) -> list[Task]:
        task_list = []
        with open(self.storage_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                task_type = row["type"]
                title = row["title"]
                date_due = datetime.strptime(row["date_due"], "%Y-%m-%d")
                completed = row["completed"].lower() == "true"
                date_created = datetime.strptime(row["date_created"], "%Y-%m-%d")

                if task_type == "recurring":
                    interval_days = int(row["interval"].split()[0])
                    interval = timedelta(days=interval_days)
                    task = RecurringTask(title, date_due, interval)
                    task.date_created = date_created
                    task.completed = completed
                    completed_dates_str = row["completed_dates"]
                    if completed_dates_str:
                        for date_str in completed_dates_str.split(";"):
                            task.completed_dates.append(datetime.strptime(date_str, "%Y-%m-%d"))
                else:
                    task = Task(title, date_due)
                    task.date_created = date_created
                    task.completed = completed

                task_list.append(task)

        return task_list

    def save_all_tasks(self, tasks: list[Task]) -> None:
        """
        Save all tasks to a CSV file.

        Args:
            tasks (list[Task]): List of task objects to be saved.
        """
        with open(self.storage_path, "w", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()

            for task in tasks:
                row = {}
                row["title"] = task.title
                row["type"] = "RecurringTask" if isinstance(task, RecurringTask) else "Task"
                row["date_due"] = task.due_date.strftime("%Y-%m-%d")
                row["completed"] = task.completed
                row["date_created"] = task.date_created.strftime("%Y-%m-%d")

                if isinstance(task, RecurringTask):
                    row["interval"] = str(task.interval.days)
                    row["completed_dates"] = ",".join(
                        [dt.strftime("%Y-%m-%d") for dt in task.completed_dates]
                    )
                else:
                    row["interval"] = ""
                    row["completed_dates"] = ""

                writer.writerow(row)


class TaskPickleDAO:
    def __init__(self, storage_path: str) -> None:
        """
        Initialize DAO with the path to the pickle file.
        """
        self.storage_path = storage_path

    def save_all_tasks(self, tasks: list[Task]) -> None:
        """
        Serialize and save the list of Task objects to a pickle file.
        """
        try:
            with open(self.storage_path, "wb") as file:
                pickle.dump(tasks, file)
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def get_all_tasks(self) -> list[Task]:
        """
        Load and deserialize the list of Task objects from the pickle file.
        Returns an empty list if file not found or error occurs.
        """
        try:
            with open(self.storage_path, "rb") as file:
                tasks = pickle.load(file)
                return tasks
        except FileNotFoundError:
            print("Pickle file not found. Returning empty task list.")
            return []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []

