#4. Valintarakenne (if) tehtävä 4.1.

kuha = float(input("Anna kuhan pituus cm: "))
alamitta = 37

if kuha < alamitta:
    puuttu = alamitta - kuha
    print("Laske kuha takaisin järveen. ") 
    print(f"{puuttu:.1f} puuttuu cm") 
else:
    print("Oikea kuhan pituus!")
    