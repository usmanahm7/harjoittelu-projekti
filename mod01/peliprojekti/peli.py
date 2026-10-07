print("---------------------------------------")
with open("mod01/peliprojekti/Intro.txt", "r", encoding='utf-8') as tiedosto:
                print(tiedosto.read())
käyttäjä = input('Anna nimesi: ')
ikä = int(input('Anna ikäsi: '))
print("---------------------------------------")

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

def reppu_valikko():
        print("---------------------------------------")
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

def luola_1():
    print("---------------------------------------")                 
    print("\nAstut pimeäänseen luolaan!!!")
    print("Luolassa on tosi hiljaista.\nLöydät lattialta vanhan aikaisen avaimen!")
    print("Avain näyttä olevan aarre laatikon avain.")
    reppu.append("Aarre-avain")
    print("Avain lisättiin reppuusi.")   

def luola_2():
    print("---------------------------------------")
    print("Luolan sisällä on kaksi reittiä.\n")

    reitti = input("Valitse vasen tai oikea retti. (v/o): ")
    if reitti == "v":
        print("---------------------------------------")
        print("Edessäsi nukkuu leijona!")
        print("Leijona heräää!!! ja hyökkää sinua päin!\n")
        print("Juokset ulos, mutta et ehtinnyt ja leijona söi sinut!")
        print("Hävisit pelin. Peli loppui.\n")
        print("Kiitos pelaamisesta!")

    elif reitti == "o":
        print("Löysit oikean, pääset seuraava tasoon")
    else:
        print("vitheellinen valinta.")
         

def peli():
    print("Peli alkaa pian..")
    print("---------------------------------------")
    print("\nOlet eksynyt metsään. Edessäsi on kaksi luolaa.")
    print("Luola 1 näyttää tosi pimeältä ja hiljaiselta.")
    print("Luola 2 näyttää tosi valoisalta, mutta kuulet jonkun eläimen äänen sieltä.")
    print("---------------------------------------")
    valinta = input("Valitse jompi kumpi luola (1 tai 2): ")  

    if valinta == "1":
        luola_1()
    elif valinta == "2":
        luola_2()
    else:
        print("virheellinen valinta.")

def ohjeet():
    print("-------------------") 
    with open("mod01/peliprojekti/Ohjeet.txt", "r", encoding='utf-8') as tiedosto:
        print(tiedosto.read())
     

if ikä < 12:
    print("Olet alaikäinen.")
else:
    print("Hauska tavata, " + käyttäjä + "!")

    while True:
        print("Valitse: 1 - peli | 2 - ohjeet | 3 - reppu | 4 - lopeta")
        komento = input("Komentoni: ")
    
        
        if komento == "1":
                peli()
        elif komento == "2":
                ohjeet()
        elif komento == "3":
                reppu_valikko()
        elif komento == "4":
                print("Kiitos pelaamisesta!\n")
                print("Tervetuloa uudestaan!!")
        else:
            print("Väärä komento. ")
                      
        