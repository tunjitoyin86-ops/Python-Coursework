from tasks import Task, RecurringTask
from task_list import TaskList
from dao import TaskCsvDAO
import datetime

class TaskManagerController:
    """
    Controls the task management system by interacting with TaskList and DAO.
    """

    def __init__(self, owner: str) -> None:
        """
        Initialize the controller with a TaskList owned by a given user.

        :param owner: Name of the task list owner.
        """
        self.task_list = TaskList(owner)

    def add_task(self, task: Task) -> None:
        """
        Add a new task to the task list.

        :param task: A Task (or subclass) object to be added.
        """
        self.task_list.add_task(task)

    def get_all_tasks(self) -> list[tuple[int, Task]]:
        """
        Return all tasks with their indexes in the list.

        :return: List of (index, task) tuples.
        """
        return self.task_list.view_tasks()

    def get_uncompleted_tasks(self) -> list[Task]:
        """
        Return only tasks that are not marked as completed.

        :return: List of uncompleted Task objects.
        """
        return self.task_list.uncompleted_tasks

    def remove_task(self, ix: int) -> None:
        """
        Remove a task from the task list using its index.

        :param ix: Index of the task to remove.
        """
        self.task_list.remove_task(ix)

    def complete_task(self, ix: int) -> None:
        """
        Mark a task as completed using its index.

        :param ix: Index of the task to mark as complete.
        """
        self.task_list.get_task(ix).mark_completed()

    def save_tasks(self, path: str) -> None:
        """
        Save all current tasks to a CSV file using the TaskCsvDAO.

        :param path: Path to the file where tasks should be saved.
        """
        dao = TaskCsvDAO(path)
        dao.save_all_tasks(self.task_list.tasks)

    def load_tasks(self, path: str) -> None:
        """
        Load tasks from a CSV file and add them to the current task list.

        :param path: Path to the file to load tasks from.
        """
        dao = TaskCsvDAO(path)
        tasks = dao.get_all_tasks()
        for task in tasks:
            self.task_list.add_task(task)
