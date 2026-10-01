class Esine:
    def __init__(self, nimi, paino):
        self.nimi = nimi
        self.paino = paino

class Huone:
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine

class Pelaaja:
    def __init__(self, nimi, sijainti):
        self.nimi = nimi
        self.esineet = []
        self.sijainti = sijainti

    def liiku(self, kohde):
        self.sijainti = kohde
        print(kohde.nimi)

    def keraa_esine(self):
        if self.sijainti.esine:
            esine = self.sijainti.esine
            self.esineet.append(esine)
            self.sijainti.esine = None
            print(esine.nimi)
        else:
            print("ei")

# Tassä ovn esineet
avain = Esine("avain", 0.1)
miekka = Esine("miekka", 3.5)

# tässä on huoneet
aula = Huone("aula", avain)
kaytava = Huone("kaytava", miekka)
varasto = Huone("varasto")

# Tässä pelaaja
nimi = input("Nimi: ")
pelaaja = Pelaaja(nimi, aula)

while True:
    print("1 huone")
    print("2 ota")
    print("3 tavarat")
    print("4 loppu")
    valinta = input("Valitse joku: ")

    if valinta == "1":
        print("1 aula")
        print("2 kaytava")
        print("3 varasto")
        kohde = input("Valitse joku: ")
        if kohde == "1": pelaaja.liiku(aula)
        if kohde == "2": pelaaja.liiku(kaytava)
        if kohde == "3": pelaaja.liiku(varasto)

    elif valinta == "2":
        pelaaja.keraa_esine()

    elif valinta == "3":
        if not pelaaja.esineet:
            print("tyhja")
        else:
            for esine in pelaaja.esineet:
                print(esine.nimi)

    elif valinta == "4":
        break
