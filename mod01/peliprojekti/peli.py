käyttäjä = input('Anna nimesi: ')
ikä = int(input('Anna ikäsi: '))

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

if ikä < 12:
    print("Olet alaikäinen.")
else:
    print("Hauska tavata, " + käyttäjä + "!")

    while True:
        print("Valitse: peli | info | lopeta")
        komento = input("Komentoni: ")

        if komento == "1":
            print("Peli alkaa pian..")
            break

        elif komento == "2":
            print("Tämä on opiskelijan tekemä peli.")

        elif komento == "3":
            print("Kiitos pelaamisesta!")

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

