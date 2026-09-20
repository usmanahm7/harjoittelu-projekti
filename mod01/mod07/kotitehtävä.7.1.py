#kotitehtävä moduuli 7 tehtävä 7.1.
import random
def heita():
    return random.randint(1,6)

while True:
    silma = heita()
    print(silma)
    if silma == 6:
        break