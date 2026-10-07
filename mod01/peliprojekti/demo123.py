print("--------------------------------")
with open("mod01/peliprojekti/Intro.txt", "r", encoding='utf-8') as tiedosto:
                print(tiedosto.read())
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

def valitse_reitti():
    print("Luolan sisällä on kaksi reittiä.")
    reitti = input("Valitse vasen tai oikea retti. (v/o): ")
    print(reitti)
    if reitti == "v":
        print("Edessäsi nukkuu leijona!")
        print("Leijona heräää!!! ja hyökkää sinua päin!")
        print("Juokset ulos, mutta et ehtinnyt ja leijona söi sinut!")
        print("Hävisit pelin. Peli loppui.")
        print("Kiitos pelaamisesta!")
        return False

    elif reitti == "o":
        print("Löysit oikean, pääset seuraava tasoon")
    else:
        print("hävisit")
    
def pelaa_luolaa():
    print("\nOlet eksynyt metsään. Edessäsi on kaksi luolaa.")
    print("Luola 1 näyttää tosi pimeältä ja hiljaiselta.")
    print("Luola 2 näyttää tosi valoisalta, mutta kuulet jonkun eläimen äänen sieltä.")
    
    valinta = input("Valitse jompi kumpi luola (1 tai 2): ")

    if valinta == "1":
        print("\nAstut pimeäänseen luolaan!!!")
        print("Se on hiljainen. Löydät lattialta vanhan aikaisen avaimen!")
        print("Avain näyttä olevan suuren aarre laatikon avain.")
        reppu.append("Aarre-avain")
        return True

    elif valinta == "2":
        peli_jatkuu = valitse_reitti()
        return peli_jatkuu

    return True


if ikä < 12:
    print("Olet alaikäinen.")
else:
    print("Hauska tavata, " + käyttäjä + "!")

    while True:
        print("Valitse: 1 - peli | 2 - ohjeet | 3 - reppu | 4 - lopeta")
        komento = input("Komentoni: ")
    
        if komento == "1":
            print("Peli alkaa pian..")
            peli_jatkuu = pelaa_luolaa()
            if not peli_jatkuu:
                break

            print("-------------------") 
            with open("mod01/peliprojekti/Ohjeet.txt", "r", encoding='utf-8') as tiedosto:
                print(tiedosto.read())

        elif komento == "3":
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
    
        elif komento == "4":
            print("---------------------")
            print("Kiitos pelaamisesta!")
            break
    
        else:
            print("Väärä komento.")
