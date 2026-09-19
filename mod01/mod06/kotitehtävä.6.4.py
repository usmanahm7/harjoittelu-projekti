#kotitehtävä moduuli 6 tehtävä 6.4.
kaupungit = []
while True:
    nimi = input("Anna joku kaupunki (Enter lopettaa): ")
    if nimi == "":
        break
    kaupungit.append(nimi)
kaupungit.sort()
for k in kaupungit:
    print(k)
