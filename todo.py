from task import Task

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def delete_task(self, index):
        del self.tasks[index]

    def update_task(self, index, new_task):
        self.tasks[index] = new_task
