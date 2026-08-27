#4. Valintarakenne (if) tehtävä 4.2.

hytti = (input("Mikä on hytti luokkasi?: "))

LUX = "parvekkeellinen hytti yläkannella."
A = "ikkunallinen hytti autokannen yläpuolella."
B = "ikkunaton hytti autokannen yläpuolella."
C = "ikkunaton hytti autokannen alapuolella."

if hytti == "LUX":
    print(LUX)
elif hytti == "A":
    print(A)
elif hytti == "B":
    print(B)
elif hytti == "C":
    print(C)
else:
    print("Tuntematon hyttiluokka. ")
