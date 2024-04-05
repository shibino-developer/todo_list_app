class Task:
    def __init__(self, title, due_date, priority, category, completed=False):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.category = category
        self.completed = completed
