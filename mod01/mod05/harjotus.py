# Kysytään käyttäjän nimi ja ikä.
käyttäjä = input('Anna nimesi: ')
# käytetään tässä int , koska ikä annetaan kokonaislukuna
ikä = int(input('Anna ikäsi: '))

# Lisätään reppu osio.
reppu = []

def lisaa_esine():
    esine = input("Anna joku esine, joka lisätään reppuusi: ")
    if esine != "":
        reppu.append(esine)
        print(esine, "lisättiin reppuusi.")
    else:
        print("Et lisännyt mitään.")

def nayta_reppu():
    if len(reppu) == 0:
        print("Reppussi on tyhjä!.")
    else:
        print("Reppusasi on: ")
        for tavara in reppu:
            print("-", tavara)

def poista_esine():
    esine = input("Anna joku esine, joka poistetaan repustasi: ")
    if esine in reppu:
        reppu.remove(esine)
        print(esine, "poistettiin repusta.")
    else:
        print("Esinettä ei löytynyt repustasi!.")


# Tarkastetaan iän perusteella, että pääseekö käyttäjä pelin sisälle.
# Jos ikä on alle 12, ilmoitetaan alaikäisyydestä ja ohjelma päättyy
# Jos ikä on 12 tai enemmän, tervehditään käyttäjää.
if ikä < 12:
    print("Olet alaikäinen.")
else:
    print("Hauska tavata, " + käyttäjä + "!")

# käyttäjältä kysytään kolme erivaihtoehtoa, josta hän päättä minkä hän itse halua tehdä.
# kirjoittamalla "lopeta" komennon peli loppuu ja tervehtii käyttäjää.
    while True:
        print("Valitse: peli | info | lopeta")
        komento = input("Komentoni: ")

        if komento == "lopeta":
            print("Kiitos pelaamisesta!")
            break

#Tässä on peli osio ja reppu valikko, jossa käyttäjä lisää esineitä, posita tai katso esineen, jonka laittoi reppuusi.
        elif komento == "peli":
            print("Peli alkaa pian...")

            print("Reppu valikko:")
            print("1) Lisää esine repuun")
            print("2) Näytä reppuni")
            print("3) Poista esine repustani")

            valinta = input("Valinta: ")

            if valinta == "1":
                lisaa_esine()
            elif valinta == "2":
                nayta_reppu()
            elif valinta == "3":
                poista_esine()
            else:
                print("Virheellinen valinta.")

        elif komento == "info":
            print("Tämä on opiskelijan tekemä peli.")
        else:
            print("Väärä komento.")
