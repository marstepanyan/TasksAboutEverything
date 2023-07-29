from composite import Manager
from leaf import Employee

if __name__ == "__main__":
    ceo = Manager("John (CEO)")

    manager1 = Manager("Alice (Manager)")
    manager2 = Manager("Bob (Manager)")

    employee1 = Employee("Tom")
    employee2 = Employee("Mary")
    employee3 = Employee("Jane")

    ceo.add(manager1)
    ceo.add(manager2)

    manager1.add(employee1)
    manager1.add(employee2)

    manager2.add(employee3)

    ceo.display()
