while True:
    menu_list ="Select option:\n1. add \n2. substract \n3. multiply \n0. exit"
    selection = input(menu_list)
    if selection == "0":
        break

numero1 = int(input("Anna numero 1"))
numero2 = int(input("Anna numero 2"))
    if selection == "1":
        print(f"Vastaus: {numero1} + {numero2} = {numero1 + numero2}")
    elif selection == "2":
         print(f"Vastaus: {numero1} - {numero2} = {numero1 - numero2}")
     elif selection == "3":
          print(f"Vastaus: {numero1} + {numero2} = {numero1 + numero2}")  
          