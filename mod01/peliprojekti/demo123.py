print("---------------------------------------")
with open("mod01/peliprojekti/Intro.txt", "r", encoding="utf-8") as tiedosto:
    print(tiedosto.read())

käyttäjä = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))
print("---------------------------------------")

reppu = []

def lisaa_esine():
    esine = input("Anna esine: ")
    if esine != "":
        reppu.append(esine)
        print(esine, "lisättiin.")
    else:
        print("Et lisännyt mitään.")

def nayta_reppu():
    if len(reppu) == 0:
        print("Reppu on tyhjä.")
    else:
        print("Reppusi sisältää:")
        for tavara in reppu:
            print("-", tavara)

def poista_esine():
    esine = input("Poista esine: ")
    if esine in reppu:
        reppu.remove(esine)
        print(esine, "poistettu.")
    else:
        print("Ei löydy repusta.")

def ohjeet():
    print("---------------------------------------")
    with open("mod01/peliprojekti/Ohjeet.txt", "r", encoding="utf-8") as tiedosto:
        print(tiedosto.read())

def luola1():
    print("---------------------------------------")
    print("Astut pimeään luolaan.")
    print("Löydät avaimen.")
    reppu.append("Aarre-avain")
    print("Aarre-avain lisättiin.")

def luola2():
    print("---------------------------------------")
    print("Luolassa on kaksi reittiä.")
    reitti = input("Valitse (v/o): ")

    if reitti == "v":
        print("Leijona hyökkää. Hävisit.")
        return False
    elif reitti == "o":
        print("Pääset seuraavaan tasoon.")
        return True
    else:
        print("Virheellinen valinta.")
        return True

def peli():
    print("Peli alkaa..")
    print("---------------------------------------")
    print("Olet eksynyt metsään. Edessäsi on kaksi luolaa.")
    valinta = input("Valitse luola (1/2): ")

    if valinta == "1":
        luola1()
    elif valinta == "2":
        if not luola2():
            return False
    else:
        print("Virheellinen valinta.")
        return True

    # OHJEET POISTETTU TÄSTÄ
    return True

def reppu_valikko():
    print("---------------------------------------")
    print("Reppu valikko:")
    print("1) Lisää")
    print("2) Näytä")
    print("3) Poista")

    valinta = input("Valinta: ")

    if valinta == "1":
        lisaa_esine()
    elif valinta == "2":
        nayta_reppu()
    elif valinta == "3":
        poista_esine()
    else:
        print("Virheellinen valinta.")

while True:
    print("Valitse: 1 - peli | 2 - ohjeet | 3 - reppu | 4 - lopeta")
    komento = input("Komentoni: ")

    if komento == "1":
        if not peli():
            break
    elif komento == "2":
        ohjeet()
    elif komento == "3":
        reppu_valikko()
    elif komento == "4":
        print("Kiitos pelaamisesta!")
        break
    else:
        print("Väärä komento.")
