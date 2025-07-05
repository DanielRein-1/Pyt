class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def intro(self):
        print(f"I am {self.name},am of {self.age} years old of age")


class Student(Person):
    def __init__(self, Person, University):
        super().__init__(Person.name, Person.age)
        self.University = University

    def intro(self):
        print(f"{self.name}, am {self.age} years i attend {self.University}")


x = Person("Daniel Rein", 21)
x.intro()

y = Student(x, "Mount kenya university")
y.intro()
