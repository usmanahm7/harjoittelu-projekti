def poista_parittomat(lista):
    parillinen_lista =[]
    for numero in lista:
        lasku = numero % 2
        if lasku == 0:
            parillinen_lista.append(numero)
    return parillinen_lista

lista =[1,7,9,13,12,24]
tulos = poista_parittomat
    