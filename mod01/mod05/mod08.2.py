nimet = set()
while True:
    nimi = input("Anna nimi, tyhjä lopettaa: ")
    if nimi == "":
        break
    if nimi in nimet:
        print("Nimi on jo joukossa")
    nimet.add(nimi)

print(nimet)