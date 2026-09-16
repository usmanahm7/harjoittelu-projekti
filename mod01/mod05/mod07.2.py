def pizzan_yksikkohinta(halkaisija, hinta):
    alue = math.pi * halkaisija**2
    result = (hinta / alue ) * 10000
    return result

halakisija1 = flaot(input("Halkaisja1: "))
hinta1 = float(input("Hinta 1: "))
halakisija2 = float(input("Halkaisija2: "))
hinta2 = float(input("Hinta 2: "))

pizza1 = pizzan_yksikkohinta(halakisija1, hinta1)
pizza2 = pizzan_yksikkohinta(halakisija2, hinta2)

if pizza1 < pizza2:
    