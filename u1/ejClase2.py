#Una pizzeria ofrece pizzas vegetarianas y no vegetarianas a sus clientes
#los ingredientes para cada tipo de piza aparecen a continuacion
#ingrediente vegetarianaos : pimiento y tofu
#ingredientes no vegetarianos: peperono, salmon y jamon
#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no
#En base a su respuesta le muestra un menu con los ingredientes disponibles
#Solo se puede elegir un ingrediente a demas del ingrediente seleccionado por defecto
#la mozarella y el tomate esta en todas las pizzas , al final debe de mostrar todos los
#ingredientes de la pizza

opcionPizza = input('Pizza a escoger Vegetariana/No Vegetariana(V/NV) ')
ingredientes=['Mozarella','Tomate']

if opcionPizza == 'V':
    print('Ingredientes\n Pimiento(P) \n Tofu(T)')
    opcionIngrediente = input('Ingrediente a escoger (P/T)')
    if opcionIngrediente == 'P':
        ingredientes.append( 'Pimiento')
    if opcionIngrediente == 'T':
        ingredientes.append( 'Tofu')
if opcionPizza == 'NV':
    print('Ingredientes\n Peperoni(P) \n Salmon(S) \n (Jamon)(J)' )
    opcionIngrediente = input('Ingrediente a escoger (P/S/J) ')
    if opcionIngrediente == 'P':
        ingredientes.append( 'Peperonni')
    if opcionIngrediente == 'S':
        ingredientes.append( 'Salmon')
    if opcionIngrediente == 'J':
        ingredientes.append( 'Jamon')

print(f'Pizza elegida {opcionPizza}, ingredientes: {", ".join(ingredientes)} ')


#Escribir un programa en el que se pregunte al usuario por una frase y una letra
# y mostrar en pantalla el numero de veces que se repite la letra

frase = input('Mencione una frase: ')
letraRepetir = input('Letra a repetir')
contador = 0 
for letra in frase:
    if letra == letraRepetir:
        contador= contador + 1

print(f'frase: {frase}, letra: {letraRepetir}, veces repetidas {contador}')
#Escribir un programa que almacene matrices, haga el producto entre ellas dos
# y muestre el resultado en una lista
#para almacenar las matrices utilice tplas anidadas
#para mostrar el resultado utilice listas anidadas

def productoMatrices(matrizA,matrizB):
    matrizC = []
    for i in range(len(matrizA)):
        matrizC.append([])
        for j in range(len(matrizB[0])):
            matrizC[i].append(0)
            for k in range(len(matrizB)):
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    return matrizC

matrizA = ((1,2,3),(4,5,6))
matrizB = ((-1,0),(0,1),(1,1))

matrizResultante = productoMatrices(matrizA,matrizB)
[print(tupla) for tupla in matrizResultante]


