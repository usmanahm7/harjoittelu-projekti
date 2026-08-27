komento = input("Anna lasku: ")
while komento != "lopeta":
    if komento == "Virhe":
        break
    print("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print("Näkemiin.")
print("Toiminnot lopetettu.")