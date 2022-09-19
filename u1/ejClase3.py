''' 
#Poblacion
Implementar una funcion llamada ordenaCiudades que reciba como argumento un diccionario
con ciudades y su poblacion; y devuelva una lista de las ciudades de mas de 200,000  habitantes ordenada de mayor a menor
'''
ciudades = {'monterrey':500000,'acapulco':400000,'cdmx':600000,'nld':100000}
def sorter(item):
    return (item[1])

def ordenaCiudads(**ciudades):
    filtered = [(key,val) for key,val in ciudades.items() if val > 200000]

    return sorted(filtered,key=sorter,reverse=True)

res = ordenaCiudads(**ciudades)
[print(val) for val in res]
'''
#Palabras
Hacer un programa que reciba como entrada una secuencia de palabras separadas por espacios en blanco e 
imprima las palabras ordenadas alfanumericamente en mayusculas y despues de haber eliminado los duplicados
'''

lorem = 'python javascript typescript java python java Typescript javascript typescript java python java typescript'

def filtrar(list):
    aux = []
    for l in list:
        if not l in aux:
            aux.append(l)
    return aux

def palabrasOrdenadas(str=''):
    palabras = str.upper().split(' ')

    filtered = filtrar(palabras)

    return sorted(filtered)

print(palabrasOrdenadas(lorem))