leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

paino = (leiviskat * 20 *32 +luodit) * 13.3
kilot = paino // 1000
grammat = paino % 1000

print(f"Massa nykymittojen mukaan: ")
print(f"{kilot} kilogramma ja {grammat:.2f} gramma. ")