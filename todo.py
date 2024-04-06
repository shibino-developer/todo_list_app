from task import Task
import json

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        del self.tasks[index]

    def update_task(self, index, new_task):
        self.tasks[index] = new_task

    def save_tasks(self, filename):
        with open(filename, 'w') as file:
            json.dump([task.__dict__ for task in self.tasks], file)
    
    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as file:
                tasks_data = json.load(file)
                self.tasks = [Task(**task_data) for task_data in tasks_data]
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty list of tasks
            self.tasks = []