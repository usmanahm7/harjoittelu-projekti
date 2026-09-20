#kotitehtävä moduuli 7 tehtävä 7.4.
def summa(lista):
    s = 0
    for l in lista:
        s += l
    return s

luvut = [3, 5, 7, 2]
print("Summa:", summa(luvut))
