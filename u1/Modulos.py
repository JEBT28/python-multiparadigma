#Modulo
import random
import csv
#from operaciones import suma, resta -> se utiliza
#cuando se quiere utilizar segmentos del archivo en especifico

#import Operaciones as op -> cuando se quiere utilizar todos los metodos y/o declaraciones 
#que existen dentro de ese archivo

#existen modulos que no vienen instalados en python
#modulos para utilizar flash, utilizar, sql... 
numRandom = random.randint(1,199)

#sirve para abrir un documento
with open("sample.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(",".join(row))

while True:
    numero = int(input("Adivine el numero entre 1 y 100"))
    if (numero== numRandom):
        break
    if(numero>numeroRandom):
        print("El numero es menor")
    else:
        print("El numero es mayor")
print(f"el numero es: {numRandom}" )