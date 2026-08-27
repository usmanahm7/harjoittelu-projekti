#Toista kunnes käyttäjä antaa negatiivisen luvun
tuumat = float(input("Anna tuumat"))

while tuumat >=0:
    print(f"{tuumat * 2.54}")
    tuumat = float(input("Anna tuumat"))
#pyytää käuyttäjää tuumääriin