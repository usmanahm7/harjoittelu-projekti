#mod05 kotitehtävä 5.2.

tuuma = float(input("Anna tuumat: "))

while tuuma >= 0:
    cm = tuuma * 2.54
    print(f"{tuuma} tuumma = {cm:.2f} cm")
    tuuma = float(input("Anna tuumat: "))
