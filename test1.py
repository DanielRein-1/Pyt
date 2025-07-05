class person:
    def __init__(self, Fname, Lname):
        self.Firstname = Fname
        self.Lastname = Lname

    def printname(self):
        print(self.Firstname, self.Lastname)


x = person("Daniel", "Rein")
x.printname()


class Student(person):
    def __init__(self, Fname, Lname):
        person.__init__(self, Fname, Lname)
        self.Middlename = "Ondoro"

    def welcome(self):
        print("welcome "+self.Middlename)


x = Student("Daniel", "Rein")
# x.printname()
print(x.Middlename)
x.welcome()
