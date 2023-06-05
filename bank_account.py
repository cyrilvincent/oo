class User:

    def __init__(self, last_name: str, first_name: str):
        self.last_name = last_name
        self.first_name = first_name

    def walk(self):
        print("I walk")

cyril = User("Vincent", "Cyril")
print(cyril)
cyril.walk()
print(cyril.first_name)