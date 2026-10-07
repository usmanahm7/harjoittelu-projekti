class Lentokone:
    def __init__(self, nimi, bensatankin_maksimi, bensatankin_nykyinen_lukema):
        self.nimi = nimi
        self.bensatankin_maksimi = bensatankin_maksimi
        self.bensatankin_nykyinen_lukema = bensatankin_nykyinen_lukema

    def tankkaa(self, kerrat):
        for i in range(kerrat):
            print(self.nimi + " tankkaa: " + self.bensatankin_nykyinen_lukema)
        return

class Lentokenttä:
    def __init__(self, nimi, bensatankin_maksimi, bensatankin_nykyinen_lukema):
            self.nimi = nimi
            self.bensatankin_maksimi = bensatankin_maksimi
            self.bensatankin_nykyinen_lukema = bensatankin_nykyinen_lukema

    def tulosta_tiedot(self, kerrat ):
         for i in range(kerrat)
            print(self.nimi )
         
         
        





