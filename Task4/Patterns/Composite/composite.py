# Composite:
# The Composite class represents composite objects,
# which are composed of one or more components (leaves or other composites).
# The Composite class implements the methods of the Component interface
# but also provides additional methods to add, remove, or access its child components.

from component import Department


class Manager(Department):
    def __init__(self, name):
        self.name = name
        self.subordinates = []

    def get_name(self):
        return self.name

    def add(self, department):
        self.subordinates.append(department)

    def remove(self, department):
        self.subordinates.remove(department)

    def display(self):
        print(f"Manager: {self.name}")
        for subordinate in self.subordinates:
            subordinate.display()
