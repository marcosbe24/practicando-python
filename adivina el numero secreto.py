#importamos "random" para mas dificultad
from random import randint
#se crea el numero secreto (en un rango del 1 al 100)
numero_secreto = randint(1,100)
#creamos un ciclo while para que tenga varios intentos
while True: 
    #pide al usuario un numero para hacer el intento
    intento = int(input("intenta adivinar el numero:"))
    if intento == numero_secreto:
        print("felicidades,lograste adivinar el numero secreto")
        #si logra adivinar entra en el if y termina el bucle
        break
    else:
        #si no,motiva a que siga intentando
        print("sigue intentando")