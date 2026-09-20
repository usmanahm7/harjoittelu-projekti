#kotitehtävä moduuli 9 tehtävä 9.1.
class Auto:
    def __init__(self, rekisteri, huippu):
        self.rekisteri = rekisteri
        self.huippu = huippu
        self.nopeus = 0
        self.matka = 0

auto = Auto("ABC-123", 142)

print("Rekisteri:", auto.rekisteri)
print("Huippunopeus:", auto.huippu)
print("Nopeus:", auto.nopeus)
print("Kuljettu matka:", auto.matka)
