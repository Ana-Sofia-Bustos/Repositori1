###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

### Completa aquí
Nom = "Sofia"
Ciutat = "Girona"
print (Nom)
print (Ciutat)

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

### Completa aquí
enter = int(12345)
floatcanvi= float(enter)
canvienter=int(3.99)
print(enter)
print(floatcanvi)
print(canvienter)



print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")


### Completa aquí

Nom1= "Sofia"
Edat = 21
Alçada = 1.58
print (f"Em dic {Nom1} tinc {Edat} anys i faig {Alçada} metres ")

print("\nExercici 5: Nombres")
print("1. Crea una variable amb el nombre PI (sense assignar una variable)")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

### Completa aquí
import math
numeropi=math.pi
arrodonit= (round(numeropi))
calcul= (arrodonit//2)
print (calcul)

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

### Completa aquí

temperatura=float(input("Ingresa la temperatura en graus celsius:"))
conversio= (temperatura*9/5)+32
print (f"la temperatura en graus celsius es {temperatura} i en graus Fahrenheit es {conversio}")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

### Completa aquí

total=float(input("Ingresa el total del compte:"))
propina=float(input("Ingresa el percentatge de propina:"))
totalpropina= total*(propina/100) # el percentatge es el total multiplicat pel percentatge/100
totalfinal=total+totalpropina
print (f"El total final es {totalfinal:.2f}")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

### Completa aquí
contrasenya=input("Ingresa una contrasenya de minim 8 caràcters:")
if len(contrasenya) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")