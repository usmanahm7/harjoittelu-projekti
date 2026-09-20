#kotitehtävä moduuli 7 tehtävä 7.3.
def gallonat_litroiksi(g):
    return g * 3.785

while True:
    g = float(input("Anna gallonat (neg lopettaa): "))
    if g < 0:
        break
    print("Litroina:", gallonat_litroiksi(g))