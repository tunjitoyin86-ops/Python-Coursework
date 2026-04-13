import tkinter as tk 
from tkinter import Frame, messagebox 
 
tasks = [] 
root = None 
tasks_listbox = None 
input_entry = None 
input_label = None 
current_input_callback = None 

def create_right_frame(root):
    raise NotImplementedError

def create_input_frame(parent):
    raise NotImplementedError
 
def create_main_window(): 
    global root 
    root = tk.Tk() 
    root.title('To Do List') 
    root.geometry('600x400+50+50') 
    root.resizable(True, True) 
    root.attributes('-topmost', 1) 
    root.columnconfigure(0, weight=1) 
    root.columnconfigure(1, weight=4) 
    root.rowconfigure(0, weight=1) 
    root.rowconfigure(1, weight=0) 
     
    left_frame = create_left_frame(root) 
    left_frame = tk.Frame(root, ...)
    left_frame.grid(column=0, row=0, sticky="nsew") 
    right_frame = create_right_frame(root) 
    right_frame.grid(column=1, row=0, sticky="nsew") 
     
    input_frame = create_input_frame(root) 
    input_frame.grid(column=0, row=1, columnspan=2, sticky="ew") 
     
    root.mainloop() 
 
def create_left_frame(parent):
 frame = tk.Frame(parent) 
 return frame
def create_right_frame(parent):
 frame = tk.Frame(parent)
 return frame
def create_input_frame(parent):
    frame = tk.Frame(parent)
    return frame

tk.Label(Frame, text="Menu", font=("Arial", 12, "bold")).pack(padx=10, pady=10) 

def add_task_gui():

 def remove_task_gui():
 
  for text, command in [("Add Task",add_task_gui), 
("Remove Task", remove_task_gui),   
("Quit", root.quit)]: 
   tk.Button(Frame, text=text, command=command).pack(padx=10, pady=5, fill=tk.X) 

def create_right_frame(parent): 
    frame = tk.Frame(parent) 
    frame.grid_rowconfigure(2, weight=1) 
    frame.grid_columnconfigure(0, weight=1) 
     
    label = tk.Label(frame, text="Tasks", font=("Arial", 12, "bold")) 
    label.grid(row=0, column=0, sticky="w", padx=5, pady=5) 
     
    global tasks_listbox 
    tasks_listbox = tk.Listbox(frame, font=("Arial", 10)) 
    tasks_listbox.grid(row=1, column=0, sticky="new", padx=5, pady=5) 
     
    return frame 
 
def create_input_frame(parent): 
    global input_label, input_entry 
    frame = tk.Frame(parent, bg="lightgray") 
    frame.columnconfigure(1, weight=1) 
     
    input_label = tk.Label(frame, text="", font=("Arial", 10), bg="lightgray") 
    input_label.grid(row=0, column=0, sticky="w", padx=10, pady=10) 
     
    input_entry = tk.Entry(frame, font=("Arial", 10)) 
    input_entry.grid(row=0, column=1, sticky="ew", padx=10, pady=10) 
    input_entry.bind("<Return>", handle_input_entry) 
     
    return frame 
 
def show_input(prompt): 
    """Display an input prompt in the bottom frame""" 
    global input_label, input_entry 
    input_label.config(text=prompt) 
    input_entry.delete(0, tk.END) 
    input_entry.focus() 
 
def handle_input_entry(event=None): 
    """Handle when user presses Enter in the input field""" 
    global current_input_callback
    if current_input_callback: 
        current_input_callback(input_entry.get()) 
        current_input_callback = None 
        hide_input() 
 
def hide_input(): 
    """Clear the input frame""" 
    input_label.config(text="") 
    input_entry.delete(0, tk.END) 
 
def update_tasks_display(): 
    global tasks_listbox 
    tasks_listbox.delete(0, tk.END) 
    for i, task in enumerate(tasks, 1): 
        tasks_listbox.insert(tk.END, f"{i}. {task}") 
 
def add_task_gui(): 
    global current_input_callback 
     
    def process_task(task): 
        if task.strip(): 
            tasks.append(task) 
            update_tasks_display() 
     
    current_input_callback = process_task 
    show_input("Enter a new task:") 
 
def remove_task_gui(): 
    if not tasks: 
        messagebox.showinfo("Info", "No tasks to remove") 
        return 
     
    def process_removal(task_num_str): 
        try: 
            task_num = int(task_num_str) 
            if 1 <= task_num <= len(tasks): 
                tasks.pop(task_num - 1) 
                update_tasks_display() 
            else: 
                messagebox.showerror("Error", f"Invalid task number. Enter 1{len(tasks)}") 
                remove_task_gui() 
        except ValueError: 
            messagebox.showerror("Error", "Please enter a valid number") 
            remove_task_gui() 
     
    global current_input_callback 
    current_input_callback = process_removal
    show_input(f"Task number to remove (1-{len(tasks)}):") 

def main(): 
 create_main_window() 
 window = tk.Tk()
 my_frame = tk.Frame(window)
 my_frame.pack()


if __name__ == "__main__": 
 main()


