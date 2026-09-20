#kotitehtävä moduuli 8 tehtävä 8.2.
nimet = set()

while True:
    nimi = input("Anna nimi (Enter lopettaa): ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("Syötetyt nimet:")
for n in nimet:
    print(n)
