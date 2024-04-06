import tkinter as tk
from tkinter import ttk
from todo import TodoList
from task import Task
import matplotlib.pyplot as plt
import json

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("600x400")
         # Set the background color of the root window
        self.root.configure(bg="#8B0000")
        self.todo_list = TodoList()

        self.task_title = tk.StringVar()
        self.due_date = tk.StringVar()
        self.priority = tk.StringVar()
        self.category = tk.StringVar()

        self.create_widgets()

        # Load tasks from file when application starts
        self.todo_list.load_tasks('tasks.json')
        self.populate_task_listbox()

        # Bind close event to save tasks before closing the application
        self.root.protocol("WM_DELETE_WINDOW", self.save_and_exit)

    def create_widgets(self):
        entry_frame = tk.Frame(self.root, bg="#FFFFFF")
        entry_frame.pack(fill="x", padx=10, pady=(10, 0))

        tk.Label(entry_frame, text="Title:", bg="#FFFFFF").grid(row=0, column=0, padx=(0, 5))
        self.task_title = tk.Entry(entry_frame, width=40)
        self.task_title.grid(row=0, column=1)

        tk.Label(entry_frame, text="Due Date:", bg="#FFFFFF").grid(row=1, column=0, padx=(0, 5), pady=5)
        self.due_date = tk.Entry(entry_frame, width=40)
        self.due_date.grid(row=1, column=1, pady=5)

        tk.Label(entry_frame, text="Priority:", bg="#FFFFFF").grid(row=2, column=0, padx=(0, 5), pady=5)
        self.priority = ttk.Combobox(entry_frame, values=["Low", "Medium", "High"], width=37)
        self.priority.grid(row=2, column=1, pady=5)
        self.priority.set("Medium")

        tk.Label(entry_frame, text="Category:", bg="#FFFFFF").grid(row=3, column=0, padx=(0, 5))
        self.category = tk.Entry(entry_frame, width=40)
        self.category.grid(row=3, column=1)

        # Buttons Frame
        button_frame = tk.Frame(self.root, bg="#FFFFFF")
        button_frame.pack(fill="x", padx=10, pady=(0, 10))

        tk.Button(button_frame, text="Add Task", command=self.add_task, bg="#8B0000", fg="white").pack(side="left", padx=(0, 5))
        tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="#8B0000", fg="white").pack(side="left", padx=(0, 5))
        tk.Button(button_frame, text="Update Task", command=self.update_task, bg="#8B0000", fg="white").pack(side="left", padx=(0, 5))
        tk.Button(button_frame, text="Show Task Stats", command=self.show_task_stats, bg="#8B0000", fg="white").pack(side="left")

        # Listbox
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, padx=10, pady=(10, 0))

        self.task_listbox = tk.Listbox(list_frame, selectmode=tk.SINGLE, bg="#F0F0F0", font=("Arial", 12), activestyle="none")
        self.task_listbox.pack(fill="both", expand=True)

    def add_task(self):
        title = self.task_title.get()
        due_date = self.due_date.get()
        priority = self.priority.get()
        category = self.category.get()
        task = Task(title, due_date, priority, category)
        self.todo_list.add_task(task)
        self.task_listbox.insert(tk.END, title)

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.todo_list.delete_task(index)
            self.task_listbox.delete(index)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            title = self.task_title.get()
            due_date = self.due_date.get()
            priority = self.priority.get()
            category = self.category.get()
            task = Task(title, due_date, priority, category)
            self.todo_list.update_task(index, task)
            self.task_listbox.delete(index)
            self.task_listbox.insert(index, title)
    
    def populate_task_listbox(self):
        # Clear the listbox and populate it with tasks
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, task.title)

    def save_and_exit(self):
        # Save tasks to file before closing the application
        self.todo_list.save_tasks('tasks.json')
        self.root.destroy()

    def show_task_stats(self):
        # Count completed tasks
        completed_tasks = sum(1 for task in self.todo_list.tasks if task.completed)
        incomplete_tasks = len(self.todo_list.tasks) - completed_tasks

        # Distribution of Tasks by Category
        categories = {}
        for task in self.todo_list.tasks:
            category = task.category
            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1

        # Plot task completion rates
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.bar(['Completed', 'Incomplete'], [completed_tasks, incomplete_tasks])
        plt.title('Task Completion Rate')
        plt.xlabel('Status')
        plt.ylabel('Number of Tasks')

        # Plot distribution of tasks by category
        plt.subplot(1, 2, 2)
        plt.bar(categories.keys(), categories.values())
        plt.title('Distribution of Tasks by Category')
        plt.xlabel('Category')
        plt.ylabel('Number of Tasks')
        plt.xticks(rotation=45, ha='right')

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
