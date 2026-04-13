from tasks import Task
import datetime

class TaskList:
    """
    Represents a list of tasks owned by a user.
    Provides methods to manage and view tasks.
    """

    def __init__(self, owner: str):
        """
        Initializes a new TaskList with an owner and an empty task list.

        :param owner: The name of the task list owner.
        """
        self.owner = owner
        self.tasks: list[Task] = []

    def get_task(self, ix: int) -> Task:
        """
        Get a task by its index.

        :param ix: The index of the task in the list.
        :return: Task at the given index.
        """
        return self.tasks[ix]

    def add_task(self, task: Task) -> None:
        """
        Add a new task to the task list.

        :param task: The task to be added.
        """
        self.tasks.append(task)

    def remove_task(self, ix: int) -> None:
        """
        Remove a task from the task list using its index.

        :param ix: The index of the task to be removed.
        """
        del self.tasks[ix]

    def view_tasks(self) -> list[tuple[int, Task]]:
        """
        Return a list of uncompleted tasks along with their indices.

        :return: List of (index, task) tuples for uncompleted tasks.
        """
        ix_tasks = []
        for task in self.uncompleted_tasks:
            # Get the index of the uncompleted task
            ix = self.tasks.index(task)
            ix_tasks.append((ix, task))
        return ix_tasks

    @property
    def uncompleted_tasks(self) -> list[Task]:
        """
        Return all tasks that are not marked as completed.

        :return: List of uncompleted tasks.
        """
        return [task for task in self.tasks if not task.completed]

    def check_task_index(self, ix: int) -> bool:
        """
        Check if the provided index is valid within the task list.

        :param ix: Index to check.
        :return: True if index is valid, False otherwise.
        """
        return 0 <= ix < len(self.tasks)
