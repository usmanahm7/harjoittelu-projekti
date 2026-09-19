#kotitehtävä moduuli 6 tehtävä 6.2.
luvut = []
while True:
    syote = input("Anna joku luku: (Enter lopetta): ")
    if syote == "":
        break
    luvut.append(int(syote))
luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)
