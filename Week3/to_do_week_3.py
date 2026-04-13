# A larger-scale Python programme 

## Task - In this exercise, we have to create a simple to-do list program using Python. Use variables, lists, input, loops, functions, and conditionals to build a basic but functional to-do list manager. 

### Import necessary libraries

import time

# Step 1: Create a list to store tasks
tasks = []

# Step 2: Define a function that allows the users to:
    # Add a new task to the list. 
    # View the current tasks in the list. 
    # Remove a task from the list. 
    # Quit and exit the program. 

# Function to add a new task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added to the todo Successfully.")

#  Function to view tasks
def view_tasks():
    print("Current todo list tasks: ")
    if not tasks:
        print("The todo list is empty.")
    else:
        for i in range(0, len(tasks)):
            print(f"Task {i+1}: {tasks[i]}")
    print(f"Total Tasks:  {len(tasks)}")

#  Function to remove a task
def remove_task():
    delete_task = int(input("Enter the task number to remove: ")) - 1
    
    # Confirm deletion
    confirm_delete = input("Are you sure you want to remove this task? (yes/no): ")
    if confirm_delete.lower() != 'yes':
        print("Task Deletion cancelled.")
    else:
        # Check if the task number is valid
        if delete_task >=0 and delete_task < len(tasks):
            remove_task = tasks.pop(delete_task)
            print(f"Task '{remove_task}' has been removed from the list successfully.")
        elif delete_task < 0 or delete_task >= len(tasks):
            print("Invalid task number. Please try again.")

# Main function to manage the to-do list
def todo_list_manager():
    print("\n To-Do List Manager:")
    print("1. Add a new task")
    print("2. View Current tasks in the list")
    print("3. Remove a task from the list")
    print("4. Quit and exit the program")

    select_option = input("Please select an option (1-4): ")
    if select_option == "1":
        add_task()
    elif select_option == "2":
        view_tasks()
    elif select_option == "3":
        remove_task()
    elif select_option == "4":
        # Confirm exiting the program
        confirm_exit = input("Are you sure you want to quit the program (yes/no): ")
        if confirm_exit.lower() != 'yes':
            print("Program exit cancelled.")
        else:
            print("You are exiting the program. It's sad to see you go, but we hope to see you again soon!")
            time.sleep(3)
            quit()
    else:
        print("Invalid option. Please try again.")

# Loop to keep the program running until the user chooses to quit
while True:
    todo_list_manager()
    print("\n")  # Print a new line for better readability