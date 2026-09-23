#Kotitehtävä moduuli 10 tehtävä 10.1.
#luodan luokka Hissille.
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        if self.kerros < self.ylin:
            self.kerros = self.kerros + 1
            print("Kerros:", self.kerros)

    def kerros_alas(self):
        if self.kerros > self.alin:
            self.kerros = self.kerros - 1
            print("Kerros:", self.kerros)

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylos()
        while self.kerros > kohde:
            self.kerros_alas()

# Tämä on koodin pääohjelma
h = Hissi(1, 8)

print("Siirto 5")
h.siirry_kerrokseen(5)

print("Siirto alin")
h.siirry_kerrokseen(h.alin)
