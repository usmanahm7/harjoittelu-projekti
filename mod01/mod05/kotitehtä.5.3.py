luvut = []

syote = input("Anna joku luku (enter lopettaa): ")
while syote != "":
    luvut.append(float(syote))
    syote = input("Anna joku luku (enter lopettaa): ")
print("Pienin luku oli:", min(luvut))
print("Suurin luku oli:", max(luvut))
