import datetime
from typing import Any
from abc import ABC, abstractmethod

class AbstractTask(ABC):
    """
    Abstract base class for all task types.
    Enforces a standard interface for task operations.
    """
    
    @abstractmethod
    def change_title(self, new_title: str) -> None:
        """Change the title of the task."""
        pass

    @abstractmethod
    def change_date_due(self, date_due: datetime.datetime) -> None:
        """Change the due date of the task."""
        pass

    @abstractmethod
    def mark_completed(self) -> None:
        """Mark the task as completed."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """String representation of the task."""
        pass


class Task(AbstractTask):
    """
    Represents a basic task with a title, creation date, due date, and completion status.
    """

    def __init__(self, title: str, date_due: datetime.datetime):
        self.title = title
        self.date_created = datetime.datetime.now()
        self.completed = False
        self.date_due = date_due

    def change_title(self, new_title: str) -> None:
        """Update the task title."""
        self.title = new_title

    def change_date_due(self, date_due: datetime.datetime) -> None:
        """Update the due date."""
        self.date_due = date_due

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def __str__(self) -> str:
        """Return a human-readable summary of the task."""
        return f"{self.title} (created: {self.date_created}, due: {self.date_due}, completed: {self.completed})"


class RecurringTask(Task):
    """
    A type of task that repeats after a fixed interval.
    Stores all dates the task was completed.
    """

    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates: list[datetime.datetime] = []

    def _compute_next_due_date(self) -> datetime.datetime:
        """Calculate the next due date based on the interval."""
        return self.date_due + self.interval

    def mark_completed(self) -> None:
        """
        Append current date to completed_dates list and
        update the next due date for the task.
        """
        self.completed_dates.append(datetime.datetime.now())
        self.date_due = self._compute_next_due_date()

    def __str__(self) -> str:
        """Return a summary including recurring status and completion history."""
        return f"{self.title} - Recurring (created: {self.date_created}, due: {self.date_due}, completed: {self.completed_dates}, interval: {self.interval})"


class PriorityTask(Task):
    """
    A task with an associated priority level:
    1 = Low, 2 = Medium, 3 = High.
    """

    PRIORITY_MAP: dict[int, str] = {
        1: "low",
        2: "medium",
        3: "high"
    }

    def __init__(self, title: str, date_due: datetime.datetime, priority: int):
        super().__init__(title, date_due)

        # Ensure only allowed priority values are used
        if priority not in self.PRIORITY_MAP:
            raise ValueError("Priority must be 1 (low), 2 (medium), or 3 (high)")
        self.priority: int = priority

    def __str__(self) -> str:
        """Return a summary with priority information included."""
        priority_str = self.PRIORITY_MAP[self.priority]
        return (f"{self.title} - Priority ({priority_str}) "
                f"(created: {self.date_created}, due: {self.date_due}, completed: {self.completed})")


class TaskFactory:
    """
    Factory class to create instances of Task, RecurringTask, or PriorityTask.
    """

    @staticmethod
    def create_task(title: str, date: datetime.datetime, **kwargs: Any) -> Task:
        """
        Return the appropriate Task subclass based on provided keyword arguments.
        - If 'interval' is given, returns RecurringTask.
        - If 'priority' is given, returns PriorityTask.
        - Else, returns a regular Task.
        """
        if "interval" in kwargs:
            return RecurringTask(title, date, kwargs["interval"])
        elif "priority" in kwargs:
            return PriorityTask(title, date, kwargs["priority"])
        else:
            return Task(title, date)
