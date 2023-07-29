# Model:
# The Model will handle the data and business logic related to the To-Do List items.
# In this case, we'll create a simple class to represent a single task.

class ToDoItem:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True
