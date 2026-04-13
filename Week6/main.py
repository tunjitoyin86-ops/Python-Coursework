from task_list import TaskList 
from users import Owner
from tasks import Task, RecurringTask
from datetime import timedelta, datetime

def propagate_task_list(task_list: TaskList) -> TaskList:
    """Propagates a task list with some sample tasks. 
    
    Args: 
        task_list (TaskList): Task list to propagate. 
    
    Returns: 
        TaskList: The propagated task list. 
    """
    # task_list.add_task("Buy groceries", "Buy groceries", datetime.now() - timedelta(days=4))
    # task_list.add_task("Do laundry", "Do laundry", datetime.now() + timedelta(days=2))
    # task_list.add_task("Clean room", "Clean room", datetime.now() - timedelta(days=1))
    # task_list.add_task("Do homework", "Do homework", datetime.now() + timedelta(days=3))
    # task_list.add_task("Walk dog", "Walk dog", datetime.now() + timedelta(days=5))
    # task_list.add_task("Do dishes", "Do dishes", datetime.now() + timedelta(days=6))

    # sample recurring task
    r_task = RecurringTask("Go to the gym", datetime.now(), timedelta(days=7))
    r_task.completed_dates.append(datetime.now() - timedelta(days=7))
    r_task.completed_dates.append(datetime.now() - timedelta(days=14))
    r_task.completed_dates.append(datetime.now() - timedelta(days=22))
    r_task.date_created = datetime.now() - timedelta(days=28)
    task_list.add_task_object(r_task)


    return task_list


def main() -> None:
    """Runs the main program loop."""
    
    # Ask user info for owner
    owner_name = input("Enter your name: ").capitalize()
    owner_email = input("Enter your email: ")

    owner = Owner(owner_name, owner_email)
    print(f"\nWelcome {owner.name}! Your email is {owner.email}")

    # Create task list with owner instance
    task_list = TaskList(owner)

    # Populate the task list with some sample tasks
    task_list = propagate_task_list(task_list)  

    # Start an infinite loop to show the menu until user chooses to exit
    while True:
        # Display the menu options
        print(f"\n To-Do List Menu - {task_list.owner.name}")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task As Completed")
        print("5. Change Task Title")
        print("6. Change Task Due Date")
        print("7. Change Task Description")
        print("8. View Overdue Tasks")
        print("9. Exit")

        # Get user choice
        choice = input("Select your option (1-9): ")

        # Handle each menu option
        if choice == "1":
            task_type = input("Do you want to add a normal task or recurring task? (normal/recurring): ").strip().lower()
            title = input("Enter a task title: ")
            desc = input("Task description: ")

            try:
                due_date_input = input("Due date (YYYY-MM-DD): ")
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d")

                if task_type == "recurring":
                    interval_days = int(input("Enter interval in days (e.g., 7 for weekly): "))
                    interval = timedelta(days=interval_days)
                    task = RecurringTask(title, due_date, interval)
                    task_list.add_task_object(task)
                else:
                    task_list.add_task(title, desc, due_date)
            except ValueError:
                print("Invalid input. Make sure your date is YYYY-MM-DD and interval is a number.")

        elif choice == "2":
            task_list.view_tasks()

        elif choice == "3":
            try:
                ix = int(input("Enter task number to remove: ")) - 1
                task_list.remove_task(ix)
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            task_list.mark_completed()

        elif choice == "5":
            task_list.change_title()

        elif choice == "6":
            task_list.change_due_date()

        elif choice == "7":
            task_list.change_description()   

        elif choice == "8":
            task_list.view_overdue_tasks()

        elif choice == "9":
            task_list.confirm_exit()

        else:
            print("Invalid option. Please try again.")

# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()
