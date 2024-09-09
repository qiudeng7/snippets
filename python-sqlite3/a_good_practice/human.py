class Human:
    def __init__(self, id,name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"