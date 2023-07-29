# Now, we can use the MVC components in our main application:

from todo_controller import ToDoController


def main():
    controller = ToDoController()

    controller.add_todo_item("Buy groceries", "Milk, eggs, bread")
    controller.add_todo_item("Finish report", "Deadline: tomorrow")
    controller.add_todo_item("Go for a run", "In the park at 6 PM")

    controller.show_todo_list()

    # Mark the first item as completed
    controller.mark_item_completed(0)

    controller.show_todo_list()


if __name__ == "__main__":
    main()
