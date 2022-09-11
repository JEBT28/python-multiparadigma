"""
Este es un comentario multilinea
"""

#Numericos
x=0
y=1
z=2

print(type(x),id(x),x)
print(type(y),id(y),y)
print(type(z),id(z),z)


#Flotantes
x=0.00
y=1.0
z=3.5

print(type(x),id(x),x)
print(type(y),id(y),y)
print(type(z),id(z),z)

#Complejos

x= 0+0j
y= 1+1j
z= 9**5+2j

print(type(x),id(x),x)
print(type(y),id(y),y)
print(type(z),id(z),z)


flotanteAEntero=2.5
enteroAFlotante=2
flotanteAComplejo=2.8

flotanteAEntero = int(flotanteAEntero)
enteroAFlotante = float(enteroAFlotante)
flotanteAComplejo=complex(flotanteAComplejo)

print(type(flotanteAEntero),id(flotanteAEntero),flotanteAEntero)
print(type(enteroAFlotante),id(enteroAFlotante),enteroAFlotante)
print(type(flotanteAComplejo),id(flotanteAComplejo),flotanteAComplejo)



#Booleanos
x = 5 
y = 6

print(y==x)

#Regresa falso si x es None(NULL)
x = None

print(bool(x))

#Regresa falso si x es dict vacio
x = {}

print(bool(x))

#Regresa falso si es una secuencia vacio
x= ()

print(bool(x))


#Cadenas
x = "mundo"
saludo = "Hola " + x
interpolate = "Hola {0}".format(x)
print(interpolate)
multilinea = '''
    {0}
    Esta es una cadena de texto multilinea
'''.format(interpolate)
print(multilinea)
print(f'Hola {x}')

print(saludo[::-1])







#metodos de lista

j = [1,2,3,4,5,6,7,8,9,10]

#Append agrega un elemento al final de la lista
j.append(11)
print(j)

#Extend agrega una lista a otra
j.extend([12,13,14,15])
print(j)

#Insert agrega un elemento en una posicion especifica
j.insert(0,0)
print(j)


#Remove elimina un elemento de la lista
j.remove(0)
print(j)


#Reverse invierte la lista
j.reverse()
print(j)

#Sort ordena la lista
j.sort()
print(j)

#Index regresa la posicion de un elemento en la lista
print(j.index(1))




'''
Sets
- No tienen indices ni indices negativos
- No se pueden agregar elementos repetidos
'''
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))

for i in s1:
    print(i)
    
    
print(3 in s1)
print(3 in s2)

#Add agregar un elemento a un set
s1.add(6)
print(s1)

#Remove elimina un elemento del set pero si no existe regresa un error
s1.remove(5)
print(s1)
#Discard elimina un elemento del set pero si no existe no regresa un error
s1.discard(6)
print(s1)
#Pop elimina aleatoriamente un elemento del set
s1.pop()
print(s1)

#Intersection regresa los elementos que se encuentran en ambos sets
s3=s1.intersection(s2)
print(s3)


'''
Diccionarios
- La llave debe ser unica
- No se puede agregar una llave que ya existe
'''

d1 = {"nombre":"Juan","apellido":"Perez","edad":20}


for key,value in d1.items():
    print(key,value) 



#Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el
#producto total.

def producto(*args):
    total = 0
    for i in args:
        total += i
    return total

total = producto(1,2,3,4,5,6,7,8,9,10)
print(total)


'''Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
posiciones múltiplos de 3, y muestre por pantalla la lista resultante.'''

abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def eliminarMultiplos(lista):
    aux= []
    for i in range(0,len(lista)-1):
        if ((i + 1) % 3) != 0:
            aux.append(lista[i])
    return aux


resultado = eliminarMultiplos(abecedario)

print(resultado)