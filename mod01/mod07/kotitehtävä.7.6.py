#kotitehtävä moduuli 7 tehtävä 7.6.
import math

def yksikkohinta(halkaisija, hinta):
    sade = halkaisija / 2
    pinta_ala = math.pi * (sade**2) / 10000
    return hinta / pinta_ala

h1 = float(input("Pizza 1 halkaisija: "))
p1 = float(input("Pizza 1 hinta: "))
h2 = float(input("Pizza 2 halkaisija: "))
p2 = float(input("Pizza 2 hinta: "))

y1 = yksikkohinta(h1, p1)
y2 = yksikkohinta(h2, p2)

if y1 < y2:
    print("Pizza 1 on edullisempi.")
else:
    print("Pizza 2 on edullisempi.")
