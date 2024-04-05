import tkinter as tk
from todo import TodoList
from task import Task
import matplotlib.pyplot as plt

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.todo_list = TodoList()

        self.task_title = tk.StringVar()
        self.due_date = tk.StringVar()
        self.priority = tk.StringVar()
        self.category = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry fields
        entry_frame = tk.Frame(self.root)
        entry_frame.pack()

        tk.Label(entry_frame, text="Title:").grid(row=0, column=0)
        tk.Entry(entry_frame, textvariable=self.task_title).grid(row=0, column=1)

        tk.Label(entry_frame, text="Due Date:").grid(row=1, column=0)
        tk.Entry(entry_frame, textvariable=self.due_date).grid(row=1, column=1)

        tk.Label(entry_frame, text="Priority:").grid(row=2, column=0)
        tk.Entry(entry_frame, textvariable=self.priority).grid(row=2, column=1)

        tk.Label(entry_frame, text="Category:").grid(row=3, column=0)
        tk.Entry(entry_frame, textvariable=self.category).grid(row=3, column=1)

        # Buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        tk.Button(button_frame, text="Add Task", command=self.add_task).pack(side="left", padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task).pack(side="left", padx=5)
        tk.Button(button_frame, text="Update Task", command=self.update_task).pack(side="left", padx=5)
        tk.Button(button_frame, text="Show Task Stats", command=self.show_task_stats).pack(side="left", padx=5)

        # Listbox
        list_frame = tk.Frame(self.root)
        list_frame.pack()

        self.task_listbox = tk.Listbox(list_frame)
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
