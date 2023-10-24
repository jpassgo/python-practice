class Person:
    def __init__(self, first_name, last_name, age, height):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height

    def __len__(self):
        return int(self.age)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age}, {self.height})"


person = Person("John", "Doe", "58", "5'11")
print(len(person))
print(person.full_name())
print(repr(person))
