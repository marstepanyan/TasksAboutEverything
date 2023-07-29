class SimpleDBMS:
    def __init__(self, db_file):
        self.db_file = db_file

    def insert(self, key, value):
        with open(self.db_file, 'a') as file:
            file.write(f"{key}={value}\n")

    def get(self, key):
        with open(self.db_file, 'r') as file:
            for line in file:
                k, v = line.strip().split('=')
                if k == key:
                    return v
        return None

    def delete(self, key):
        with open(self.db_file, 'r') as file:
            lines = file.readlines()
        with open(self.db_file, 'w') as file:
            for line in lines:
                k, v = line.strip().split('=')
                if k != key:
                    file.write(f"{k}={v}\n")

    def display_all(self):
        with open(self.db_file, 'r') as file:
            for line in file:
                print(line.strip())


dbms = SimpleDBMS("db.txt")

dbms.insert("name", "James")
dbms.insert("age", "33")
dbms.insert("city", "New York")
print("Display all: ")
dbms.display_all()
print()
print("Display only name: ")
print("Name:", dbms.get("name"))
print()
print("Delete age, and display: ")
dbms.delete("age")
dbms.display_all()
