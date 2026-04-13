# Import the datetime module to work with dates and times
import datetime

class Task:
    """Represents a task in a to-do list."""

    def __init__(self, title: str, due_date: datetime.datetime, description: str = "") -> None:
        """
        Creates a new task with a title, due date

        Args:
            title (str): What the task is about.
            due_date (datetime): When the task should be finished.
            description (str): A short explanation about the task (optional).

        """
        self.title = title  # the name or title of the task
        self.completed = False  # task is not done yet
        self.date_created = datetime.datetime.now()  # time the task was created
        self.due_date = due_date  # when the task is due
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
            f"Task: {self.title} | Description: {self.description} | "
            f"Completed: {status}{completed_info} | "
            f"Created on: {self.date_created.strftime('%Y-%m-%d')} | "
            f"Due: {self.due_date.strftime('%Y-%m-%d')} "
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

class RecurringTask(Task):
    """Represents a recurring task in a to-do list.
    Args:
    Task (Task): The task to be repeated.
    """
    def __init__(self, title: str, date_due: datetime.datetime, interval: datetime.timedelta):
        """Creates a new recurring task.
        Args:
        title (str): Title of the task.
        date_due (datetime.datetime): Due date of the task.
        interval (datetime.timedelta): Interval between each repetition.
        """
        super().__init__(title, date_due)
        self.interval = interval
        self.completed_dates : list[datetime.datetime] = [] # list of datetime.datetime objects

    def _compute_next_due_date(self) -> datetime.datetime:
        """Computes the next due date of the task.
        Returns:
        datetime.datetime: The next due date of the task.
        """
        return self.due_date + self.interval
    
    def mark_completed(self) -> None:
        """
        Marks the recurring task as completed by:
        - Adding the current date to the completed_dates list.
        - Updating the due_date to the next due date using the interval.

        Overrides the base Task.mark_completed method.
        """
        now = datetime.datetime.now()
        self.completed_dates.append(now)
        self.date_completed = now
        self.due_date = self._compute_next_due_date()
        self.completed = True
        print(f"Recurring Task '{self.title}' marked as completed on {now.strftime('%Y-%m-%d %H:%M')}.")
        print(f"Next due date is now {self.due_date.strftime('%Y-%m-%d')}.")

        
    def __str__(self) -> str:
        return f"{self.title} (Recurring) | Due: {self.due_date.strftime('%Y-%m-%d')} | Interval: {self.interval.days} days | Completed on: {[d.strftime('%Y-%m-%d') for d in self.completed_dates]}"
