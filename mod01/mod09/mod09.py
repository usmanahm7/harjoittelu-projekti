class auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinen_nopeus = 0
        self.kuljettu_matka = 0
    def kiihdyta(self, muutos):
        if self.tämänhetkinen_nopeus muutos <= 0:
            self.tämänhetkinen_nopeus = 0
        elif self.tämänhetkinen_nopeus + muutos >= self.huippunopeus:
            self.tämänhetkinen_nopeus = self.huippunopeus
        else:
            self.tämänhetkinen_nopeus += muutos


auto1 = auto("ABC-123",142)
auto1.kiihdyta(30)
auto1.kiihdyta(70)
auto1.kiihdyta(50)

print(f"Auton noppeus nyt: {auto1.huippunopeus}")


