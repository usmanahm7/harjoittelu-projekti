asemat = []
while True:
    valinta = input("1.Lisää lentoasema \n2. Hae asemaa \n3.Lopeta")
    if valinta == "1":
        iceao = input("Anna asema ICEAO koodi:")
        nimi = input("Anna asema nimi: ")
        asemat[iceao] = nimi
    if valinta == "2":
        icao = input("Anna aseman ICAo koodi: ")
        print(f"Aseman nimi on: {asemat[iceao]}")
    if valinta == "3":
        break



