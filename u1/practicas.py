'''
#1 Funciones con n parámetros
Escribir un programa que contenga una función que reciba n parámetros de tipo numérico y calcule el
producto total.
'''

from datetime import date

def producto(*args):
    total = 1
    for i in args:
        total *= i
    return total

productoTotal = producto(1,2,3,4,5,6,7,8,9,10)
print(productoTotal)

'''
#2 Manejo y manipulación de elementos de una lista
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen
posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
'''

eliminarMultiplosDeTres = lambda lista: [lista.remove(i) for i in lista if (lista.index(i) + 1) % 3 == 0]

abecedario = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

eliminarMultiplosDeTres(abecedario)

print(abecedario)

'''
#3 Entrada de datos y manipulación.
Escribir un programa que permita al usuario capturar su nombre completo e imprima su nombre de
manera inversa letra por letra
'''

nombre = input('Ingresa tu nombre completo: ')

for letra in nombre[::-1]:
    print(letra)


'''
#4 Entrada de datos y estructuración.
Revisar su retícula para escribir un programa que cree un diccionario vacío para que el usuario capture
las materias y créditos de su semestre preferido (inferior a 8vo) al final imprimir en el formato
“{asignatura}” tiene “{créditos}” créditos. Y la suma de todos los créditos del semestre
'''

materias = {}

while True:
    
    materia = input('Ingresa el nombre de la materia: ')
    creditos = int(input('Ingresa el número de créditos: '))
    
    materias[materia] = creditos
    
    continuar = input('¿Deseas agregar otra materia? (s/n): ')
    
    if continuar == 'n':
        break
totalCreditos = 0
for materia,creditos in materias.items():
    totalCreditos += creditos
    
    print(f'{materia} tiene {creditos} créditos')
    
print(f'El total de créditos del semestre es {totalCreditos}')


'''
#5 Manejo de información
Escribir una función que reciba n parámetros de llave valor e imprima la información en formato
“{llave}”: “{Valor}”
'''

def imprimirDict(**kwargs):
    for llave,valor in kwargs.items():
        print(f'{llave}: {valor}')


datos = {'nombre':'Juan Esteban','apellido':'Baltierrez Tobon','edad':22, 'carrera':'Ingeniería de Sistemas', 'nControl': '18100152'}

imprimirDict(**datos)



'''
#6 Razonamiento y prueba de código
Escribir un programa que reciba un numero entre 0 y 20 e imprimir el numero en letra, no utilizar
condicionales, máximo 5 líneas de código.
'''

numeroALetra = lambda numero: ['cero','uno','dos','tres','cuatro','cinco','seis','siete','ocho','nueve','diez','once','doce','trece','catorce','quince','dieciseis','diecisiete','dieciocho','diecinueve','veinte'][numero]

print(numeroALetra(20))
print(numeroALetra(0))
print(numeroALetra(5))

'''
#7 Formateo y conversiones
Escribir un programa que muestre un menú con 2 opciones la primera opción “1.- Imprimir
YYYY/MM/DD” la segunda “2.- Imprimir MM/DD/YYYY” una vez seleccionada la opción imprimir la fecha
del día de hoy en el formato seleccionado. 
'''
from datetime import date

def imprimirFecha(opcion):
    fecha= date.today()
    if opcion == 1:
        print(f'{fecha.year}/{fecha.month}/{fecha.day}')
    elif opcion == 2:
        print(f'{fecha.month}/{fecha.day}/{fecha.year}')
    else:
        print('Opción no válida')


opcion = int(input('''
                   Opciones de fecha:
                   1.- Imprimir YYYY/MM/DD
                   2.- Imprimir MM/DD/YYYY

                   Ingresa la opción deseada: '''))

imprimirFecha(opcion)

'''
#8 Resumen y multi-solución
8.1.-Definir una clase usuario que contenga como atributos:
-Usuario
-Contraseña
-Rol
-Nombre
-CURP
-Ciudad
'''

class Usuario:
    
    usuario = ''
    contrasena = ''
    rol= 'cliente'
    nombre = ''
    curp = ''
    ciudad = ''
    
    def __init__(self,usuario,contrasena,nombre,curp,ciudad,rol='cliente'):
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.curp = curp
        self.ciudad = ciudad
        self.rol = rol

    #toString
    def __str__(self):
        return f'Usuario: {self.usuario} \nContraseña: {self.contrasena} \nRol: {self.rol} \nNombre: {self.nombre} \nCURP: {self.curp} \nCiudad: {self.ciudad}'

'''
8.2.-Realizar un programa que contenga el siguiente menú
1.- Registro
2.- Inicio de sesión
3.- Salida
'''
usuarioAdministrador = Usuario('admin','admin','Administrador','123456789','NLD','administrador')
usuarios = [usuarioAdministrador]

def validarInicioSesion(nombre,contrasena):
    aux = [usuario for usuario in usuarios if usuario.usuario == nombre and usuario.contrasena == contrasena]
    
    if len(aux) > 0:
        return aux[0]
    else :
        return None

def imprimirInfo(**kwargs):
    for llave,valor in kwargs.items():
        print(f'{llave}: {valor}')
    print('---------------------------------')
        
mostrarUsuarios = lambda: [imprimirInfo(**usuario.__dict__) for usuario in usuarios]

def registrarUsuario():
    usuario = input('Ingresa el nombre de usuario: ')
    contrasena = input('Ingresa la contraseña: ')
    nombre = input('Ingresa tu nombre: ')
    curp = input('Ingresa tu CURP: ')
    ciudad = input('Ingresa tu ciudad: ')
    
    nuevoUsuario = Usuario(usuario,contrasena,nombre,curp,ciudad)
    
    existe= [usuario for usuario in usuarios if usuario.curp == nuevoUsuario.curp]
    
    if len(existe) > 0:
        print('El usuario ya existe')
    else:
        usuarios.append(nuevoUsuario)
        
def iniciarSesion():
    usuario = input('Ingresa el nombre de usuario: ')
    contrasena = input('Ingresa la contraseña: ')
    existe = validarInicioSesion(usuario,contrasena)
    
    if not existe:
        print('Usuario o contraseña incorrectos')
        return
    if existe.rol == 'administrador':
        print('Bienvenido administrador')
        print('Lista de usuarios\n---------------------------------')
        mostrarUsuarios()
    else:
        print(f'Bienvenido {existe.nombre}')
    
    return

'''Inicio'''


while True:
    opcion = int(input('''
                   Opciones:
                   1.- Registro
                   2.- Inicio de sesión
                   3.- Salida

                   Ingresa la opción deseada: '''))
    
    if opcion == 1:
        registrarUsuario()
    elif opcion == 2:
        iniciarSesion()
    elif opcion == 3:
        break
    else:
        print('Opción no válida')
