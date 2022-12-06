#Ejercicio 1 prueba 3 

import random

def numero_aleatorio():
    return random.randint(1,100)

def Revisar (numero,dori):   
    print (numero)
    if numero == dori:
        print ("El numero ingresa es correcto")
        return True
    elif (numero > dori):
        print ("El numero ingresado es muy alto")
        return False
    else:
        print ("El numero ingresado es muy bajo")
        return False
       
while True:
    nemo = numero_aleatorio()
    for i in range(10):
        numero_ingresado = int(input("Ingrese un numero entre el 1 y 100: "))
        if Revisar(numero_ingresado, nemo):
            break
    print ("El numero es: " + str(nemo))