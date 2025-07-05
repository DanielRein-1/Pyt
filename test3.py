class Human:
    def __init__(self, legs, hands):
        self.legs = legs
        self.hands = hands

    def Looks(self):
        print(f"Human have  {self.legs}  legs and  {self.hands}  hands.")


class SuperHuman(Human):
    def __init__(self, legs, hands, Power):
        super().__init__(legs, hands)
        self.Power = Power


def looks(self):
    print(f"SuperHumans have {self.legs} legs, {self.hands} hands")


x = Human(2, 2)
x.Looks()

y = SuperHuman(2, 2, "Invincible")
y.Looks()
