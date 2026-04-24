#9-misol
class Sportchi:
    def __init__(self, ism):
        self.ism = ism

    def oyin(self):
        print("O‘ynayapti")


class Futbolchi(Sportchi):
    def oyin(self):
        print("Futbol o‘ynayapti")


s1 = Futbolchi("Ronaldo")
s1.oyin()
