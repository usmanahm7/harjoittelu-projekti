#kotitehtävä moduuli 6 tehtävä 6.1.
import random

maara = int(input("Montako arpakuutiota? "))

luvut = []

for _ in range(maara):
    luvut.append(random.randint(1, 6))

summa = 0
for luku in luvut:
    summa += luku

print(summa)
