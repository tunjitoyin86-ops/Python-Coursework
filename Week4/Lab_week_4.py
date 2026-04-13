## I. PYTHON CLASSES
### Exercise 1: Creating Classes and Initializing Objects.
# check this for more information.https://uws-primo.hosted.exlibrisgroup.com/permalink/f/1a10t95/44PAI_ALMA5183288570003931

### Import necessary libraries

import sys
import time
import datetime

# Define Task class:
class Task:

 def __init__(self, title, date_due):
        self.title = title
        self.completed = False
        self.date_created = datetime.datetime.now()
        self.date_due = date_due

def __str__(self):
        status = "Yes" if self.completed else "No"
        return(f"Task: {self.title} - completed: {status} ")
    
def mark_completed(self):
        self.completed = True
        print(f"Task '{self.title}' marked as completed.")

def change_title(self, new_title):
        old_title = self.title
        self.title = new_title
        print(f"Task title has changed from '{old_title}' to '{new_title}'. ")

# TaskList class definition
class TaskList:
    def __init__(self, owner):
        self.owner = owner.capitalize()
        self.tasks = []
     
# Method to add a new task object
    def add_task(self, task):
        self.tasks.append(task)
        date_created = datetime.datetime.now()
        print(f"Task '{task.title}' has been added Successfully on '{date_created.strftime("%c")}'.")
        
#  Method to remove a task by index 
def remove_task(self,ix):
# Check if the task number is valid
        if ix in range(len(self.tasks)):
            
# Confirm deletion
            confirm_delete = input("Are you sure you want to remove this task? (yes/no): ")
            if confirm_delete.lower() != 'yes':
             print("Task Deletion cancelled.")
        else:
         removed_task = self.tasks[ix]
        del self.tasks[ix] # get and also remove task
        print(f"Task '{removed_task.title}' has been removed successfully.")
    
        print("Invalid index. No task removed.")
        self.conditions()

#  Method to view all tasks
def view_tasks(self):
        if not self.tasks:
            print("The todo list is empty.")
            self.conditions()
        else:
            print("\nCurrent Tasks: ")
            for index, task in enumerate(self.tasks, start=1):
                print(f"\n {index}. {task} . Created on . {task.date_created.strftime('%Y-%m-%d')} . and Due on: {task.date_due.strftime('%Y-%m-%d')}")

# Method to mark a task completed 
def mark_completed(self):
        self.view_tasks()
        try:
            print(len(self.tasks))
            complete_task_id = int(input("\nEnter the completed task number: "))
            if 0 <= complete_task_id < len(self.tasks):
                self.tasks[complete_task_id-1].mark_completed()
                self.view_tasks()
                self.conditions()
            else:
                print("Invalid task number")
                self.conditions()
        except ValueError:
            print("Please enter a valid number")
            self.conditions()
    
# Method to change task title
def change_title(self):
        self.view_tasks()
        try:
            print(len(self.tasks))
            to_change_id = int(input("Enter the task number to change the task: "))
            if 0 <= to_change_id <= len(self.tasks):
                new_title = input("Enter the new Task Title: ")
                self.tasks[to_change_id-1].change_title(new_title)
                self.view_tasks()
                self.conditions()
            else:
                print("Invalid task number")
                self.conditions()
        except ValueError:
            print("Please enter a valid number")
            self.conditions()

# Confirm exiting the program
def confirmExit(self):
 confirm_exit = input("Are you sure you want to quit the program (yes/no): ")
 if confirm_exit.lower() != 'yes':
                print("Exit cancelled.")
                self.conditions()
 else:
      print("Goodbye! Hope to see you again soon!")
      time.sleep(3)
      sys.exit() # This will stop the whole method of running
    
# Ask user if they want to do something else
def conditions(self):
        condition = input("Do you want to perform another activity? (yes/no): ")
        if condition.lower() == "yes":
            self.list_options()
        elif condition.lower() == "no": 
            self.confirmExit()
        else:
            print("Invalid choice. Please choose between yes/no")
            self.conditions()

# Method to display the menu and handle user choices
def list_options(self):
        print("\n To-Do List Manager:")
        print("1. Add a new task")
        print("2. View Current tasks in the list")
        print("3. Remove a task from the list")
        print("4. Mark a task as completed")
        print("5. Change the title of a task")
        print("6. Quit and exit the program")

        select_option = input("Please select an option (1-6): ")
        if select_option == "1":
            title = input("Enter the task: ")
            input_date = input("Enter tasks' due date (YYYY-MM-DD): ")
            date_object = datetime.datetime.strptime(input_date, "%Y-%m-%d")
            task = task(title, date_object)
            self.add_task(task)
            self.conditions()
        elif select_option == "2":
            self.view_tasks()
            self.conditions()
        elif select_option == "3":
            self.view_tasks()
            try:
                index = int(input("Enter the task number to be removed: ")) -1
                self.remove_task(index)
                self.conditions()
            except ValueError:
                print("Please enter a valid number")
        elif select_option == "4":
            self.mark_completed()
            self.conditions()
        elif select_option == "5":
            self.change_title()
            self.conditions()
        elif select_option == "6":
            self.confirmExit()
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
            self.conditions()

# Program Start
owner = input("Enter your name: ")
my_tasks = TaskList(owner)
print(my_tasks.owner)

print(f"\n Welcome {my_tasks.owner}! \n")

# Add sample tasks before entering the main loop
# my_tasks.tasks = [
#     Task("Do Homework"),
#     Task("Do Laundry"),
#     Task("Go Shopping")
# ]

# View the tasks
my_tasks.view_tasks()

# Main loop
while True:
    my_tasks.list_options()


