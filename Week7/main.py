from task_list import TaskList 
from users import Owner
from tasks import Task, RecurringTask
from datetime import timedelta, datetime
from dao import TaskCsvDAO , TaskPickleDAO 

def main() -> None:
    """Runs the main program loop."""

    # Ask user info for owner
    owner_name = input("Enter your name: ").capitalize()
    owner_email = input("Enter your email: ")
    owner = Owner(owner_name, owner_email)
    print(f"\nWelcome {owner.name}! Your email is {owner.email}")

    # Create empty task list
    task_list = TaskList(owner)

    while True:
        # Show menu
        print(f"\n To-Do List Menu - {task_list.owner.name}")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task As Completed")
        print("5. Change Task Title")
        print("6. Change Task Due Date")
        print("7. Change Task Description")
        print("8. View Overdue Tasks")
        print("9. Load Tasks from DAO")
        print("10. Save Tasks to DAO")
        print("11. Load Tasks from Pickle File")
        print("12. Save Tasks to Pickle File")
        print("13. Exit")

        choice = input("Select your option (1-13): ")

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
                print("Invalid date or interval.")

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
            file_path = input("Enter file path to load tasks from: ")
            dao = TaskCsvDAO(file_path)
            loaded_tasks = dao.get_all_tasks()
            for task in loaded_tasks:
                task_list.add_task_object(task)
            print("Tasks loaded successfully.")

        elif choice == "10":
            file_path = input("Enter file path to save tasks to: ")
            dao = TaskCsvDAO(file_path)
            dao.save_all_tasks(task_list.tasks)
            print("Tasks saved")

        elif choice == "11":
            file_path = input("Enter Pickle file path to load tasks from: ")
            dao = TaskPickleDAO(file_path)
            loaded_tasks = dao.get_all_tasks()
            for task in loaded_tasks:
                task_list.add_task_object(task)
            print("Tasks loaded from Pickle.")

        elif choice == "12":
            file_path = input("Enter Pickle file path to save tasks to: ")
            dao = TaskPickleDAO(file_path)
            dao.save_all_tasks(task_list.tasks)
            print("Tasks saved to Pickle file.")

        elif choice == "13":
            task_list.confirm_exit()

        else:
            print("Invalid option. Please try again.")


# Run the main function only if this file is executed directly
if __name__ == "__main__":
    main()
