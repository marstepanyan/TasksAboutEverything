# Leaf:
# The Leaf class represents individual objects or leaves in the composition.
# These are the simplest building blocks and do not have any children.
# Leafs implement the methods defined in the Component interface.

from component import Department


class Employee(Department):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def display(self):
        print(f"Employee: {self.name}")
