###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

senyal = float(input("Ingresa el nivell de senyal rebut en dBm: "))
if senyal >= -50:
    print (f" la {senyal} es excel·lent")
elif -50 <= senyal < -67:
    print(f"la {senyal} es bona")
elif -67 <= senyal <-75:
    print (f"la {senyal}es feble")
else:
    print (f"la {senyal} es molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.


potencia = float(input("Ingresa la potencia de la connexió de la dibra optica en dBm:"))
if -27 <= potencia <= -8:
    print (f"la {potencia} de la connexió es acceptable")
elif potencia > -8:
    print (f"la {potencia} de la connexió es massa alta")
else:
    print (f"la {potencia} de la connexió es massa baixa")


# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum = float(input("Ingresa el consum de dades en GB:"))
if consum > 20:
    limit = consum-20
    print (f"El consum de dades ha superat el limit de 20GB amb {limit} GB adiccionals")
else:
    print ("El consum de dades es troba dins del limit de 20GB")


# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

indicadorLOS = int(input("Indica si l'indicador LOS està encès (1 per sí, 0 per no): "))
indicadorROU = int(input("Indica si l'indicador del ROUTER està encès (1 per sí, 0 per no): "))

# Entenc que LOS encès (1) significa "Loss Of Signal" (fallida física)
if indicadorLOS == 1:
    print("Ha de revisar el cable de fibra")
elif indicadorLOS == 0 and indicadorROU == 0:
    print("Ha de revisar el servei del proveïdor")
else:
    # Si no hi ha alarma de cable ni falta de servei, tot funciona
    print("La connexió sembla funcionar correctament")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria = int(input ("Indica el percentatge de bateria del SAI:"))
if bateria < 0 or bateria > 100:
    print("Percentatge indicat fora de rang")
elif bateria < 20:
    print("La bateria del SAI és crítica")
elif 20 <= bateria <= 49:
    print("La bateria del SAI és baixa")
else:
    print("La bateria del SAI és suficient")


# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Ingresa la latencia en mil·lisegons: "))
perdua= int(input("Ingresa la perdua en percentatge:"))
if latencia <0 or  perdua <0 or perdua >100:
    print ("La latencia o la perdua es troben fora de rang, latencia <0 o perdua <0 o perdua>100")
elif latencia <= 30 and perdua <=1:
    print ("la connexió es excel·lent")
elif latencia <= 80 and perdua <=3:
    print ("la connexió es bona")
elif latencia <=150 and perdua <=5:
    print ("la connexió es acceptable")
else:
    print ("la connexió es deficient")



# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.

pla = int(input("Quin és el tipus de pla? (basic (1) o plus (0)): "))
consum = float(input("Ingresa el consum mensual en GB: "))

if (pla != 0 and pla != 1) or consum < 0:
    print("Pla desconegut o consum negatiu")
elif pla == 1:
    if consum <= 10:
        print("El cost del pla bàsic és de 10 €")
    else:
        cost = 10 + (consum - 10) * 1.50
        print(f"El cost total del pla bàsic és de {cost} €")
elif pla == 0:
    if consum <= 30:
        print("El cost del pla plus és de 20 €")
    else:
        cost = 20 + (consum - 30) * 0.75
        print(f"El cost total del pla plus és de {cost} €")

# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.

compte = int(input("Indica si el compte és actiu (1) o inactiu (0): "))
contrasenyacorrecta = int(input("Indica si la contrasenya és correcta (1=Sí, 0=No): "))

if contrasenyacorrecta == 0 and compte == 0:
    print("El compte és inactiu i la contrasenya no és correcta")
elif contrasenyacorrecta == 0 and compte == 1:
    print("El compte és actiu però la contrasenya no és correcta")
elif contrasenyacorrecta == 1 and compte == 0:
    print("La contrasenya és correcta però el compte és inactiu")
elif contrasenyacorrecta == 1 and compte == 1:
    codi = int(input("Indica si el codi és correcte (1=Sí, 0=No): "))
    if codi == 1:
        print("Accés concedit")
    else:
        print("Accés denegat")

    
# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.
router = int (input ("Indica si el router està encès (1)si, (0)No:"))
terminal = int (input("Indica si l'indicador LOS del terminal optics està encès (1)si, (0)No:"))
internet = int (input("Indica si l'indicador d'internet està encès (1)si, (0)No:"))
if router == 0:
    print ("router apagat, si us plau encengui el router")
elif router ==1:
    if terminal ==1:
        print ("cal revisar el cable de fibra")
    elif terminal == 0 and internet ==0:
        print ("cal contactar amb el el proveidor de internet ")
    elif terminal == 0 and internet ==1:
        print ("la connexió sembla funcionar correrctament")




# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

incidencia= int (input ("indica si la incidència afecta un servei critic 1(SI), 0 (NO):"))
usuaris = int (input("indica el nombre d'usuaris afectats:"))
alternativa = int (input ("indica si existeix una alternativa de connexió 1(SI), 0 (NO):"))
if usuaris < 0:
    print("Nombre d'usuaris no vàlid (no pot ser negatiu)")
elif (incidencia == 1 and alternativa == 0)  or (alternativa == 0 and usuaris >= 50):
    print ("incidencia de prioritat critica")
elif usuaris >=10 or incidencia == 1:
    print ("incidencia de prioritat alta")
else:
    print ("incidencia de prioritat baixa ")
#PER FER COMPARACIONS SEMPRE NUMERO PETIT A L'ESQUERRA AL MIG VARIABLE I NUMERO GRAN A LA DRETA AIXI SEMPRE ELS SIGNES MIREN CAP A L'ESQUERRA
#VARIABLE DINS D'UN RANG
#Posa el número petit a l'esquerra (10). 
# Posa la variable al mig (usuaris).
# Posa el número gran a la dreta (50).
# Posa tots els signes apuntant a l'esquerra (< o <=):