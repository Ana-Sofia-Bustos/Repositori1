paraules1 = ["casa", "arbre", "sol", "elefant", "lluna", "cotxe"]
comptador=0
lletra = input("ingressa una lletra:")
for paraula in paraules1:
    primera_lletra= paraula[0]
    if lletra == primera_lletra:
        comptador+=1
print (comptador)
    