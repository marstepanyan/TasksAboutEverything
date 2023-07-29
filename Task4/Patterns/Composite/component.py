# Component:
# The Component is an abstract class or interface that defines the common interface for all objects in the composition,
# whether they are leaf nodes (individual objects) or composite nodes (groups of objects).
# It declares methods that are applicable to both types of objects.

from abc import ABC, abstractmethod


class Department(ABC):
    @abstractmethod
    def get_name(self):
        pass

    def add(self, department):
        pass

    def remove(self, department):
        pass

    def display(self):
        pass
