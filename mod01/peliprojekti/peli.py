# Kysytään käyttäjän nimi ja ikä.
käyttäjä = input('Anna nimesi: ')
# käytetään tässä int , koska ikä annetaan kokonaislukuna
ikä = int(input('Anna ikäsi: '))

# Tarkastetaan iän perusteella, että pääsekö käyttäjä pelin sisälle.
if ikä < 12:
    print("Olet alaikäinen.")
else:
    print("Hauska tavata, " + käyttäjä + "!")
    
    while True:
        print("Valitse: peli | info | lopeta")
        komento = input("Komentoni: ")
        
        if komento == "lopeta":
            print("Kiitos pelaamisesta!")
            break
        elif komento == "peli":
            print("Peli alkaa pian...")
        elif komento == "info":
            print("Tämä on opiskelijan tekemä peli.")
        else:
            print("Väärä komento.")

# Jos ikä on alle 12, ilmoitetaan alaikäisyydestä ja ohjelma päättyy
# Jos ikä on 12 tai enemmän, tervehditään käyttäjää.
# käyttäjältä kysytään kolme erivaihtoehtoa, josta hän päättä minkä ite halua tehdä.
# kirjoittamalla "lopeta" komennon peli loppuu ja tervehtii käyttäjää.