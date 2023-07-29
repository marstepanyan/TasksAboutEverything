# View:
# The View will handle the presentation of the To-Do List to the user.
# For simplicity, we'll use a basic text-based interface.

class ToDoView:
    def show_todo_list(self, todo_list):
        for index, item in enumerate(todo_list):
            status = " [x] " if item.completed else " [ ] "
            print(f"{index + 1}. {status} {item.title} - {item.description}")
        print()
        