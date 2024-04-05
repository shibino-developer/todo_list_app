class Task:
    def __init__(self, title, due_date=None, priority=None, category=None):
        self.title = title
        self.due_date = due_date
        self.priority = priority
        self.category = category
