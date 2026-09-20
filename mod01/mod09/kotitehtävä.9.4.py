#kotitehtävä moduuli 9 tehtävä 9.4.
import random

class Auto:
    def __init__(self, rek, huippu):
        self.rek = rek
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippu:
            self.nopeus = self.huippu
        if self.nopeus < 0:
            self.nopeus = 0

    