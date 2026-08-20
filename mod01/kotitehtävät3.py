#kotitehtävä 3. Muuttujat ja vuorovaikutteiset ohjelmat
#tehtävä 3.2.

import math

sade_str = input("Anna ympyrän säde: ")
sade = float(sade_str)
pinta_ala = math.pi * sade**2
print(f"Ympyrän pinta-ala: {pinta_ala}")