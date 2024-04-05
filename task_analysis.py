# task_analysis.py

class Task:
    def __init__(self, title, completed, category):
        self.title = title
        self.completed = completed
        self.category = category

# Define some tasks (replace this with your actual list of tasks)
tasks = [
    Task("Task 1", True, "Planning"),
    Task("Task 2", False, "Requirement Analysis"),
    Task("Task 3", True, "Design"),
    Task("Task 4", False, "Development"),
    Task("Task 5", True, "Deployment")
]

# Task Completion Rates
completed_tasks = sum(task.completed for task in tasks)
incomplete_tasks = len(tasks) - completed_tasks

print("Completed tasks:", completed_tasks)
print("Incomplete tasks:", incomplete_tasks)

# Distribution of Tasks by Category
categories = {}
for task in tasks:
    category = task.category
    if category in categories:
        categories[category] += 1
    else:
        categories[category] = 1

print("Distribution of Tasks by Category:")
for category, count in categories.items():
    print(category, ":", count)
