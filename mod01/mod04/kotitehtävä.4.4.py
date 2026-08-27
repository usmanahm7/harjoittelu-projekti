#4. Valintarakenne (if) tehtävä 4.4.

#Kysytään vuosilukua käyttäjältä.
vuosi = int(input("Anna vuosiluku: "))

#katsotaan karkausvuosia
#jaollinen neljällä  ja 400:lla on karkausvuosi. 
if vuosi % 400 == 0:
    print("Vuosi on karkausvuosi!: ")
elif vuosi % 100 == 0:
    print("Vuosi ei ole karkausvuosi!!: ")
elif vuosi % 4 == 0:
    print("Vuosi on karkausvuosi!!: ")
else:
    print("Vuosi ei ole karkausvuosi!: ")
