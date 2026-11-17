###
# EXERCICIS (range)
###

# Exercici 1: Imprimir números de l'1 al 10
# Imprimeix els números de l'1 al 10 (inclosos) fent servir un bucle for i range().

for num in range (1,11):
    print (num)

# Exercici 2: Imprimir números senars de l'1 al 20
# Imprimeix tots els números senars entre 1 i 20 (inclosos) fent servir un bucle for i range().

senars =[]
for numero in range (1,21):
    if numero %2 !=0:
        senars.append(numero)
print (senars)


# Exercici 3: Imprimir múltiples de 5 (MULTIPLE ES NUMERO% 5 == 0)
# Imprimeix els múltiples de 5 des del 5 fins al 50 (inclosos) fent servir un bucle for i range().

multiples =[]
for numero in range (5,51):
    if numero %5 ==0:
        multiples.append(numero)
print (multiples)


# Exercici 4: Imprimir números en ordre invers
# Imprimeix els números del 10 a l'1 (inclosos) en ordre invers fent servir un bucle for i range().
for num in range (10,0,-1):
    print (num)

# Exercici 5: Suma de números en un rang
# Calcula la suma dels números de l'1 al 100 (inclosos) fent servir un bucle for i range().
suma = 0
for num in range (1,101):
    suma+=num
print (suma)


# Exercici 6: Taula de multiplicar
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle for i range().
taula = []
numero = int(input("Introdueix un numero:"))
for i in range (1,11):
    multiplicacio=numero*i
    taula.append(multiplicacio)
print (taula)
