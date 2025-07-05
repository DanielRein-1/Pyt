class animal:
    def __init__(self, Animal):
        self.Animal = Animal

    def pname(self):
        print(self.Animal + " has 4 legs")


x = animal("Lion")
# print(x.Animal)
x.pname()


class animal1(animal):
    def __init__(self, Animal):
        super().__init__(Animal)
        self.Animal = Animal

    def Pname(self):
        print(self.Animal)


x = animal1("cow")
x.pname()
# print(x.Animal)
# x.Pname()
