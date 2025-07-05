class person:
    def __init__(self, Fname, Lname):
        self.Firstname = Fname
        self.Lastname = Lname

    def printname(self):
        print(self.Firstname, self.Lastname)


x = person("Daniel", "Rein")
x.printname()


class Student(person):
    pass


x = Student("Ondoro", "Rein")
x.printname()
