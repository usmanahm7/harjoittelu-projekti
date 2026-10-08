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

        print("---------------------------------------")
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
    print("Luolassa on tosi hiljaista.")
    print("\nLöydät lattialta vanhan aikaisen avaimen!\n")
    print("Avain näyttä olevan aarre laatikon avain.\n")
    reppu.append("Aarre-avain")
    print("Avain lisättiin reppuusi.\n")   

def luola1_jatkuu():
     print("Jatkat matkaasi luolan perään\nNäet siellä kaksi arkkua")
     print("\nmutta sieltä yhdestä kuuluu kobran ääni.\nJos valitsen väärän arkkun")
     print("niin myrkyllinen kobra tapppaa sinut ja häviät pelin!")

     valinta = input("Valitse yksi arkuista (1 tai 2): ")

     if valinta == "1":
        print("---------------------------------------")
        print("Avaat lukollisen arkun aarre-avaimellasi.")
        print("\n Arkkuu avautuu hitaasti...")
        print("Sisältää paistaa kultainen valoaa\n")
        print("Näet kulta kolikkoita ja timannteja!!\n")
        reppu.append("Kulta kolikot ja timantit")
        print("\nkulta kolikot ja timantit lisättiin repuussi.")
        print("\nLöysit kadonneen aarreen!\n")
        print("---------------------------------------")
        print("Voitit peliin!! Onneksi olkoo.")
        print("Kiitos pelaamisesta. Tervetuloa uudestaan.\n")
     elif valinta =="2":
        print("---------------------------------------")
        print("\nSisältää kuuluu kobran äänii!!!\n")
        print("Kobraa iskee!!!")
        print("---------------------------------------")
        print("\nHävisit pelin. Peli loppui.")
        print("Kiitos pelaamisesta.")
        print("---------------------------------------")
        exit()
     else:
        print("Virheellinen valinta.")



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
        exit()

    elif reitti == "o":
        print("Onneksi olkoon pääsit oikeaan reittiin!")
        print("Pääset seuraava tasoon")
        print("------------------------")
        print("\nLuola näyttää olevan osa metsän suojelualuetta.")
        print("\nKuljet oikeaa reittiä pitkin...")
        print("---------------------------------------")
        print("\nNäet ison oven edessäsi.\n Sammalla näet ison susin nukkuvan.\n")
        print("Susi vielä nukkuu, mutta et voi tehdä kovaa  ääntä!.")
        print("\nMitä teet?")
        print("\nValitse oikea vaihtoehtoa päästäksesi eteenpäin!")
        print("-----------------------------------------")
        print("Valinta 1: Menee Susin vierestä ohi hiljaan.")
        print("\nValinta 2: Harhauta susia heittämällä kiveä kauas.")     

        valinta = input("\nValiste vaihtoehto (1 tai 2):\n")
        print("-------------------------")
        
        if valinta == "1":
            print("Susi heräsi!!!")
            print("\nHyökkäsi sinua päin, ja tappoi sinut!!")
            print("Hävisit peli")
            print("-----------------------")
            print("Kiitos pelaamisesta. Tervetuloa uudestaan.")
            exit()
        
        elif valinta == "2":
            print("Susi herää ja harhautuu kiven perään...")
            print("\nJuokset ovesta ulos ja ehdit sulkea ennen\nkuin susi huomaa.\n")
            print("Näet edessäsi kiiltä timanttin ja ulos käynnin luolasta.")
            reppu.append("Timantti")
            print("\nTimantti lisättiin reppuusi")
            print("Pääset luolasta ulos elossa ja löysit yksi aarreista.\n")
            print("---------------------------------")
            print("Onneksi olkoon voitit pelin.")
            print("Kiitos pelaamisesta.\n")
            exit()

    else:
        print("virheellinen valinta.")
         

def peli():
    print("Peli alkaa pian..")
    print("---------------------------------------")
    print("\nOlet eksynyt metsään. Edessäsi on kaksi luolaa.\n")
    print("Luola 1 näyttää tosi pimeältä ja hiljaiselta.")
    print("Luola 2 näyttää tosi valoisalta,\nmutta kuulet jonkun eläimen äänen sieltä.")
    print("---------------------------------------")
    valinta = input("Valitse jompi kumpi luola (1 tai 2): ")  

    if valinta == "1":
        luola_1()
        luola1_jatkuu()
        
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
    print("---------------------------------------")

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
                print("---------------------------------------")
                print("Kiitos pelaamisesta!\n")
                print("Tervetuloa uudestaan!!")
        else:
            print("Väärä komento. ")
                      
        