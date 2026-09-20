#kotitehtävä moduuli 9 tehtävä 9.3.
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

    def kulje(self, tunnit):
        self.matka += self.nopeus * tunnit
