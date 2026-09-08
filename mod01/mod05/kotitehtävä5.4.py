#kotitehtä mod05 kotitehtävä 5.4.

import random

numero = random.randint(1, 10)
print("Arvaa lukua väliltä 1..10.: ")

arvaus = int(input("Anna arvaus: "))

while arvaus != numero:
    if arvaus > numero:
        print("Arvauso on liian suuri. ")
    else:
        print("Arvaus on liian pieni. ")
    arvaus = int(input("Anna arvaus: "))
print("Oikein! ")