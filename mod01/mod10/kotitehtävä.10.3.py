#Kotitehtävä moduuli 10 tehtävä 10.3.
#tehtävä 10.2 jatkuu
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

#luodan luokka Talolle.
class Talo:
    def __init__(self, alin, ylin, lkm):
        self.hissit = []
        for _ in range(lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, nro, kohde):
        print("Hissi", nro, "kohteeseen", kohde)
        self.hissit[nro].siirry_kerrokseen(kohde)
#lisätään uus metodi palohälytys        
    def palohalytys(self):
        print("Palohalytys")
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin)

#Tämä on pääohjelmaa.
t = Talo(1, 8, 2)

t.aja_hissia(0, 5)
t.aja_hissia(1, 3)
t.aja_hissia(0, 1)
t.palohalytys()