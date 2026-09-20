#kotitehtävä moduuli 8 tehtävä 8.1.
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät",
              "kesä", "kesä", "kesä", "syksy", "syksy",
              "syksy", "talvi")

kk = int(input("Anna kuukauden numero (1-12): "))
print("Vuodenaika:", vuodenajat[kk - 1])
