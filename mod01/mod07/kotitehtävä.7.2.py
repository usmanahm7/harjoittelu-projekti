#kotitehtävä moduuli 7 tehtävä 7.2.
import random
def heita(tahkot):
    return random.randint(1, tahkot)
tahkot = int(input("Anna nopan tahkojen määrä: "))
while True:
    silma = heita(tahkot)
    print("Silmäluku:", silma)
    if silma == tahkot:
        break
