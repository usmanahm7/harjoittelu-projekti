#kotitehtävä moduuli 7 tehtävä 7.5.
def karsi_parittomat(lista):
    uusi = []
    for l in lista:
        if l % 2 == 0:
            uusi.append(l)
    return uusi

luvut = [1, 2, 3, 4, 5, 6]
print("Alkuperäinen:", luvut)
print("Karsittu:", karsi_parittomat(luvut))
