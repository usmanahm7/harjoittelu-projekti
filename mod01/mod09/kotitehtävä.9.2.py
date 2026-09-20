#kotitehtävä moduuli 9 tehtävä 9.2.
class Auto:
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippu:
            self.nopeus = self.huippu
        if self.nopeus < 0:
            self.nopeus = 0

auto = Auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print("Nopeus:", auto.nopeus)

auto.kiihdyta(-200)
print("Nopeus hätäjarrutuksen jälkeen:", auto.nopeus)
