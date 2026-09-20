#kotitehtävä moduuli 8 tehtävä 8.3.
asemat = {}

while True:
    toiminto = input("Syötä (uusi/haku/lopeta): ")

    if toiminto == "lopeta":
        break

    if toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        asemat[icao] = nimi

    elif toiminto == "haku":
        icao = input("Anna ICAO-koodi: ")
        if icao in asemat:
            print("Lentoasema:", asemat[icao])
        else:
            print("Ei löydy.")
