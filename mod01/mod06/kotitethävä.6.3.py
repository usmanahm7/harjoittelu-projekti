#kotitehtävä moduuli 6 tehtävä 6.3.
n = int(input("Anna joku kokonaisluku: "))

if n < 2:
    print("Ei ole alkuluku.")
else:
    alkuluku = True
    for i in range(2, n):
        if n % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")