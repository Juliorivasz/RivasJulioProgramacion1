from funciones import create_id_partner
'''1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.'''

def dni_Valid(dni):
    # valida si esta entre 7 y 8 digitos, pero antes convierte el numero de dni en cadena y obtiene la longitud 
    if  6 < len(str(dni)) < 9:
        return True
    else:
        return False
    
# print(dni_Valid(9610448355)) # False
# print(dni_Valid(25933770)) # True

'''2.	Escribir una función que, dado un string, retorne la longitud de la última palabra. Se considera que las palabras están separadas por uno o más espacios. 
También podría haber espacios al principio o al final del string pasado por parámetro.'''

# def ultimate_Str(text):
#     ultimate_Word = text.split()
#     long_Word = len(ultimate_Word[-1])
#     return  long_Word

# print(ultimate_Str("Hola, soy julio"))

'''3.	Escribir un programa que permita al usuario obtener un identificador para cada uno de los socios de un club. 
Para eso ingresará nombre completo y número de DNI de cada socio, indicando que finalizará el procesamiento mediante el ingreso de un nombre vacio.'''

# diccionario para almacenar a los socios
patner = {}
while True:
    # solicita el ingreso del nombre completo
    name_partner = input("Ingresa tu nombre completo, dejar vacio para salir: ")
    # separa el nombre completo en partes
    name = name_partner.split()
    # validacion de salida del while
    if name_partner == "":
        break
    # primer nombre
    first_name = name[0]
    # apellido
    last_name = name[-1]
    # segundo nombre en caso de tenerlo
    if len(name) > 2:
        second_name = name[1]
    elif len(name) > 3:
        last_name = name[3]
    # dni
    dni_partner = input("Ingresa tu dni: ")
    # valida el dni
    while not dni_Valid(dni_partner):
        dni_partner = input("Ingrese un DNI correcto: ")
    # funcion para crear el identificador
    identity = create_id_partner(first_name,second_name,last_name,dni_partner)
    patner[name_partner] = identity
    
print(patner)

