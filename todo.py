from task import Task

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def update_task(self, index, task):
        if 0 <= index < len(self.tasks):
            self.tasks[index] = task

    def get_task(self, index):
        if 0 <= index < len(self.tasks):
            return self.tasks[index]

    def __len__(self):
        return len(self.tasks)
