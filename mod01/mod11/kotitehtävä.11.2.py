#Kotitehtävä moduuli 11 tehtävä 11.2.
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
# Tässä om Aliluokat sahko ja polttomotori auto.
class Sahkoauto(Auto):
    def __init__(self, rekisteri, huippu, akku):
        super().__init__(rekisteri, huippu)
        self.akku = akku

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteri, huippu, tankki):
        super().__init__(rekisteri, huippu)
        self.tankki = tankki