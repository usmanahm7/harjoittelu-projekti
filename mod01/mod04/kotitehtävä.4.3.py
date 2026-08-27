#4. Valintarakenne (if) tehtävä 4.3.

#kysytään käyttäjältä sukupuoli.
sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ")

#kysytään heemoglobi arvoa käyttäjältä.
hb = int(input("Anna hemoglobiarvo (g/l): "))

#laitetaan arvot mitä saatin mies ja naisen paikalle.
if sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobi on alhainen: ")
    elif hb <= 195:
        print("Hemoglobi on normaali: ")
    else:
        print("Hemoglobi on korkea!: ")

if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobi on alhainen: ")
    elif hb <= 175:
        print("Hemoglobi on normaali: ")
    else:
        print("Hemoglobi on korkea!: ")
