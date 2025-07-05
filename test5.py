class Animals:
    def __init__(self, Legs, Head):
        self.Legs = Legs
        self.Head = Head

    def details(self):
        print(f"Animals have {self.Legs} legs and {self.Head} head")
        print("Animals can also speak")


class Dog(Animals):
    def __init__(self, Animals, Speak):
        super().__init__(Animals.Legs, Animals.Head)
        self.Speak = Speak


def details(self):
    print(f"A dog has {self.legs} legs, {self.head} head, and it {self.speak}")


x = Animals(4, 1)
x.details()

y = Dog(x, "Barks")
y.details()
