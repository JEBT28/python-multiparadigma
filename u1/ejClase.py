'''
Funciones
Escribir un programa que reciba una cadena de caracteres y 
devuelva un diccionario con cada palabra que contiene y su longitud

Escribir un programa que reciba un diccionario y devuelva 
una tupla con la palabra mas repetida y su frecuencia
'''

def dictLongitudPalabra(str):
    palabras = str.split(' ')
    dict = {}
    for palabra in palabras:
        if not palabra in dict:
            dict[palabra] = 0
        dict[palabra]+= 1
    return dict

str = 'Hola mundo Hola'
dict = dictLongitudPalabra(str)
print(dict)


'''

'''

def palabraMasRpetida(**dict):
    llaveMayor = ''
    for key in dict.keys():
        if len(llaveMayor) == 0:
            llaveMayor = key
        if key == llaveMayor:
            continue
        elif dict[key] >= dict[llaveMayor]:
            llaveMayor = key
        return (llaveMayor,dict[llaveMayor])

print(palabraMasRpetida(**dict))


'''
Tipo de datos
Una jugueteria tiene mucho exito en unos de sus productos : payasos y muñecas,
suele hacer su venta por correo y la empresa de logistica les cobra x peso del paquete,
deben de calcular el peso de los payasos y muñecas que se dan en cada paquete  
c/payaso = 112gr
c/muñeca = 75gr

Escribir un programa que lea el numero de payasos y muñecas,y calcule el peso total del paquete
que sera enviado y el precio total del envio
100gr/payaso = $2.5
100gr/muñeca = $2.0 
'''



def calcularEnvio(payasos, muñecas):
    
    pesoPayasos = payasos*112
    pesoMuñecas = muñecas*75
    
    costoPayasos = (pesoPayasos / 100 ) * 2.5
    costoMuñecas = (pesoMuñecas / 100 ) * 2
    
    costoTotal = costoPayasos+costoMuñecas
    pesoTotal = pesoPayasos + pesoMuñecas
    
    
    return (pesoTotal,costoTotal)


payasos = int(input('Ingrese el numero de payasos: '))
muñecas = int(input('Ingrese el numero de muñecas: '))

pesoTotal,costoTotal = calcularEnvio(payasos=payasos, muñecas=muñecas)

print(f'Peso total: {pesoTotal} gr      Costo total: ${costoTotal}')
    
    
    

'''
Escribir un programa que pregunte el nombre de un producto,
su precio y un numero de unidades y muestre en pantalla una
cadena con su informacion '{producto} {precio} {unidades} {costoTotal}'
'''

producto = input('Producto: ')
costo = float(input('Costo: '))
unidades = int(input('Unidades: '))

costoTotal = costo* unidades
print(f'Producto: {producto}\nPrecio: ${costo: 6.2f}\nUnidades: {unidades}\nCosto total: ${costoTotal: 8.2f}')

