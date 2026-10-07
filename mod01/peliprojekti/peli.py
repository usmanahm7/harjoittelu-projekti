print("Tervetuloa pieneen seikkailuun peliin.")
print("Tavoitteesi on löytää kadonnut avain.")

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
        print("Valitse: 1 - peli | 2 - ohjeet | 3 - reppu | 4 - lopeta")
        komento = input("Komentoni: ")
    
        if komento == "1":
            print("Peli alkaa pian..")

            print("\nOlet eksynyt metsään. Edessäsi on kaksi luolaa.")
            print("Luola 1 näyttää tosi pimeältä ja hiljaiselta.")
            print("Luola 2 näyttää tosi valoisalta, mutta kuulet jonkun eläimen äänen sieltä.")
            
            valinta = input("Valitse jompi kumpi luola (1 tai 2): ")
    
            if valinta == "1":
                print("\nAstut pimeäänseen luolaan!!!")
                print("Se on hiljainen. Löydät lattialta vanhan aikaisen avaimen!")
                print("Avain näyttä olevan suuren aarre laatikon avain.")
                reppu.append("Aarre-avain")

            elif valinta == "2":
                print("Näät edessä ison karhun nukkuvan!")
                print("Karhu heräää!!! ja hyökkää sinua päin!")
                print("Juokset ulos, mutta et ehtinnyt ja karhu söi sinut!")
                print("Hävisit pelin. Peli loppui.")
                print("Kiitos pelaamisesta!")

        elif komento == "2":
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
            print("Kiitos pelaamisesta!")
            break
    
        else:
            print("Väärä komento.")
