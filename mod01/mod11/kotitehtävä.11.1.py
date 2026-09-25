#Kotitehtävä moduuli 11 tehtävä 11.1.
# Julkaisu on yliluokka
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
#Kirja ja Lehti ovat aliluokkia
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirja: {self.nimi}")
        print(f" Kirjoittaja: {self.kirjoittaja}")
        print(f" Sivumäärä: {self.sivumaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print(f"Lehti: {self.nimi}")
        print(f" Päätoimittaja: {self.paatoimittaja}")


# Tämä on koodin Pääohjelma.
aku_ankka = Lehti("Aku Ankka", "Aki Hyyppä")
hytti6 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

aku_ankka.tulosta_tiedot()
hytti6.tulosta_tiedot()
