# Controller:
# The Controller will act as the intermediary between the Model and the View,
# handling user interactions and updating the Model accordingly.

from todo_item import ToDoItem
from todo_view import ToDoView


class ToDoController:
    def __init__(self):
        self.todo_list = []

    def add_todo_item(self, title, description):
        item = ToDoItem(title, description)
        self.todo_list.append(item)

    def mark_item_completed(self, item_index):
        if 0 <= item_index < len(self.todo_list):
            self.todo_list[item_index].mark_as_completed()

    def show_todo_list(self):
        view = ToDoView()
        view.show_todo_list(self.todo_list)
        