
class Hahmo:
    def __init__(self, nimi, repliikki):
        self.nimi = nimi
        self.repliikki = repliikki
        self.hp = 100

class Pelaajahahmo(Hahmo):
    def __init__(self, nimi, hp, tavaralista):
        super().__init__(nimi, hp)
        self.tavarat = tavaralista

    def tulosta_tavarat(self):
        print("Hahmolla on:")
        for t in self.tavarat:
            print(t)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        self.tulosta_tavarat()
        print("\n")


class Hirviö(Hahmo):
    def __init__(self, nimi, repliikki):
        self.nimi = nimi
        self.repliikki = repliikki
        self.hp = 100
        self.hahmo = None
        super().__init__(pelaajahahmo)
        

    def tulosta_tiedot(self):
        print(f"Hahmon nimi: {self.nimi}")
        print(f"Hahmon hp: {self.hp}")

    def taistelu(self, vastustaja):
        print("Tulee suuri taistelu.")
        input()
        if vastustaja.hp > self.hp:
            print(f"{self.nimi} hävisi taistelun :<")
            self.hp = 0
        else:
            print(f"{self.nimi} voitti taistelun!")
            self.tulosta_tiedot()

merihirvio = Hahmo("Merihirviö", "Lits läts, aion syödä sinut!")
pelaajahahmo = Hahmo(input("Anna hahmon nimi: "), "Olen sankari ja voitan kaikki!")

print("Peli alkaa.")
pelaajahahmo.tulosta_tiedot()
input()

print(f"{pelaajahahmo.nimi} kohtaa ensimmäiseksi kauhean hirviön. Hirviö huutaa:")
print(merihirvio.repliikki)
merihirvio.tulosta_tiedot()

input()
pelaajahahmo.taistelu(merihirvio)
input()
print(f"Peli ohi.")


