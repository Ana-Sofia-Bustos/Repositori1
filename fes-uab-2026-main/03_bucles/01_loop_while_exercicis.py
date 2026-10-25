###
# EXERCICIS (while)
###

# Exercici 1: Compte enrere
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

comptador= 10
while comptador >=1 :
    print (comptador)
    comptador -=1

# Exercici 2: Suma de números parells (while)
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

comptador1 = 1
suma = 0
while comptador1 <= 20:
    numero = comptador1
    comptador1 += 1 
    if numero % 2 != 0:
        continue
    suma += numero
print(suma)

# Exercici 3: Factorial d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

numero1= int(input("ingressa un numero enter positiu:"))
factorial = 1 #el factorial multiplica per tant si el poso a 0 donara 0 sempre, 0 per una suma si estaria be
while numero1>=0 :
    factorial = factorial *numero1
    numero1 -= 1
print (factorial)
    

# Exercici 4: Validació de contrasenya
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".


contrasenya = input("ingressa una contrasenya:")
while len(contrasenya) <8:
    print ("la contrasenya no es valida, ha de tenir minim 8 caracters")
    contrasenya = input("ingressa una contrasenya:")
else:
    print ("contrasenya valida")

# Exercici 5: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

numero2= int(input("ingressa un numero:"))
taula=1
while numero2 >=1 and taula <=10:
    multiplicacio= numero2*taula
    taula+=1
    print (multiplicacio)


# Exercici 6: Números primers fins a N
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

N= int(input("ingressa un numero enter positiu:"))
primers=2 #2 per que es el primer numero primer
while True:
    if N>=1 and primers<=N:
        es_primer=True
        divisor=2
        while divisor<primers:
           if primers%divisor==0:
            es_primer=False
            break
           divisor+=1
        if es_primer ==True:
            print(primers)
        primers+=1
    else:
        break


# Exercici 7: Suma fins al zero
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.


sumador=0
enters= int(input("introdueix un numero enter:"))
while enters !=0:
    sumador+=enters
    enters= int(input("introdueix un numero enter:")) 
print (sumador)


# Exercici 8: Comptar les xifres d'un número
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.


# Exercici 9: Seqüència de Fibonacci
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.

# Exercici 10: Joc d'endevinar el número
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.
