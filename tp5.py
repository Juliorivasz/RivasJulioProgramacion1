
from funciones import (sum_digit,create_id_partner,are_prime,calc_temp_medium,add_space,find_max_min,calculate_circle_area_perimeter,login,apply_off,apply_function,create_dictionary_words,
calc_module,is_prime,calculator_factorial,get_numbers,calculator_frequency)
'''1.	Escribir una función que, dado un número de DNI, retorne True si el número es válido y False si no lo es. 
Para que un número de DNI sea válido debe tener entre 7 y 8 dígitos.'''

# def dni_Valid(dni):
#     # valida si esta entre 7 y 8 digitos, pero antes convierte el numero de dni en cadena y obtiene la longitud 
#     if  6 < len(str(dni)) < 9:
#         return True
#     else:
#         return False
    
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

# while True:
#     # solicita el ingreso del nombre completo
#     name_partner = input("Ingresa tu nombre completo, dejar vacio para salir: ")
#     # separa el nombre completo en partes
#     name = name_partner.split()
#     # validacion de salida del while
#     if name_partner == "":
#         break
#     # primer nombre
#     first_name = name[0]
#     # apellido
#     last_name = name[-1]
#     # segundo nombre en caso de tenerlo
#     if len(name) > 2:
#         second_name = name[1]
#     elif len(name) > 3:
#         last_name = name[2]
#     # dni
#     dni_partner = input("Ingresa tu dni: ")
#     # valida el dni usa la funcion del ejercicio 1
#     while not dni_Valid(dni_partner):
#         dni_partner = input("Ingrese un DNI correcto: ")
#     # funcion para crear el identificador
#     identity = create_id_partner(first_name,last_name,dni_partner)
# # muestra el identificador
# print(f"ID => {identity}")

'''4.	Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es múltiplo del otro. Crea una función que reciba los dos números, 
y devuelve si el primero es múltiplo del segundo.'''

# num_1 = int(input("ingrese un primer numero entero: "))
# num_2 = int(input("ingrese el segundo numero entero: "))

# if are_prime(num_1, num_2):
#     print("El primer numero es primo del segundo")
# elif num_2 % num_1 == 0:
#     print("El segundo numero es primo del primero")
# else:
#     print("Ninguno de los numeros son primos entre si")

'''5.	Crear una función que calcule la temperatura media de un día a partir de la temperatura máxima y mínima. Crear un programa principal, 
que utilizando la función anterior, vaya pidiendo la temperatura máxima y mínima de cada día y vaya mostrando la media. El programa pedirá el número de días 
que se van a introducir.'''

# # Programa principal
# def main():
#     # Pedir al usuario el número de días
#     num_days = int(input("Ingrese el número de días: "))
    
#     # Ciclo para ingresar las temperaturas de cada día y calcular la media
#     for day in range(1, num_days + 1):
#         temp_max = float(input(f"Ingrese la temperatura máxima del día {day}: "))
#         temp_min = float(input(f"Ingrese la temperatura mínima del día {day}: "))
        
#         # Calcular la temperatura media utilizando la función
#         temp_media = calc_temp_medium(temp_max, temp_min)
        
#         # Mostrar la temperatura media del día
#         print(f"Temperatura media del día {day}: {temp_media} °C")

# main()

'''6.	Crea una función que reciba como parámetro un texto y devuelve una cadena con un espacio adicional tras cada letra. Por ejemplo, 
“Hola, tú” devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha función.'''

# # Programa principal
# def main():
#     # Pedir al usuario que ingrese un texto
#     text = input("Ingrese un texto: ")
    
#     # Llamar a la función y mostrar el resultado
#     text_with_space = add_space(text)
#     print("Texto con espacios adicionales tras cada letra:")
#     print(text_with_space)

# main()

'''7.	Crea una función que recibe una lista con valores numéricos y devuelve el valor máximo y el mínimo. 
Crea un programa que pida números por teclado y muestre el máximo y el mínimo, utilizando la función anterior.'''

# # Programa principal
# def main():
#     # Pedir al usuario que ingrese números separados por espacios
#     numbers = input("Ingrese números separados por espacios: ")
    
#     # Convertir la entrada del usuario en una lista de números
#     list_numbers = [float(numbers) for numbers in numbers.split()]
    
#     # Llamar a la función para encontrar el máximo y el mínimo
#     maxim, minim = find_max_min(list_numbers)
    
#     # Mostrar el máximo y el mínimo
#     if maxim is not None and minim is not None:
#         print(f"El valor máximo es: {maxim}")
#         print(f"El valor mínimo es: {minim}")
#     else:
#         print("La lista está vacía, no hay máximo ni mínimo.")

# main()

'''8.	Diseñar una función que calcule el área y el perímetro de una circunferencia. Utiliza dicha función en un programa principal que lea el radio de una circunferencia y 
muestre su área y perímetro.'''

# # programa principal
# def main():
#     # Pide al usuario que ingrese el radio del círculo.
#     radius = float(input("introduce el radio del circulo: "))
    
#     # Llama a la función para calcular el área y el perímetro.
#     area, perimeter = calculate_circle_area_perimeter(radius)
    
#     # Muestra el área y el perímetro.
#     print(f"El area del circulo es: {area:.2f}")
#     print(f"El perimetro del circulo es: {perimeter:.2f}")

# main()

'''9.	Crear una subrutina llamada “login”, que recibe un nombre de usuario y una contraseña y te devuelve Verdadero si el nombre de usuario es “usuario1” y 
la contraseña es “asdasd”. Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido hacer login incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una contraseña y se intente hacer login, solamente tenemos tres oportunidades para intentarlo.
'''

# # Programa principal
# def main():
#     attemps = 0
#     max_attemps = 3
    
#     # Pedir al usuario el nombre de usuario y la contraseña
#     while attemps < max_attemps:
#         user = input("Ingrese el nombre de usuario: ")
#         password = input("Ingrese la contraseña: ")
        
#         # Llamar a la función login para verificar el acceso
#         acces, attemps = login(user, password, attemps)
        
#         if acces:
#             print("¡Inicio de sesión exitoso!")
#             break
#         else:
#             print("Nombre de usuario o contraseña incorrectos. Inténtalo de nuevo.")
    
#     if attemps >= max_attemps:
#         print("Has alcanzado el número máximo de intentos. Acceso denegado.")

# main()

'''10.	Escribir una función que aplique un descuento a un precio. Esta función tiene que recibir un diccionario con los precios y 
porcentajes del carrito de compra, aplicar los descuentos a los productos del carrito  y devolver el precio final de la compra.'''

# # Diccionario de productos y sus porcentajes de descuento
# offs = {
#     "product1": 10,  # 10% de descuento para producto1
#     "product2": 5,   # 5% de descuento para producto2
#     "product3": 15   # 15% de descuento para producto3
# }

# # Diccionario que representa el carrito de compras (producto: precio)
# cart_shop = {
#     "product1": 50,
#     "product2": 30,
#     "product3": 40
# }

# # Llamar a la función para calcular el precio final después de aplicar descuentos
# price_final = apply_off(cart_shop,offs)

# # Mostrar el precio final de la compra después de aplicar descuentos
# print(f"Precio final de la compra después de aplicar descuentos: {price_final}")

'''11.	Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de aplicar la función dada a cada uno de los elementos de la lista.'''

# # Ejemplo de función que puede ser pasada como argumento
# def square(number):
#     return number ** 2

# # Ejemplo de lista de números
# numbers = [1, 2, 3, 4, 5]

# # Llamar a la función aplicar_funcion() con la función cuadrado y la lista de números
# result = apply_function(square, numbers)

# # Mostrar el resultado
# print("Lista original:", numbers)
# print("Lista después de aplicar la función cuadrado:", result)

'''12.	Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene y su longitud.'''

# # Pedir al usuario que ingrese una frase
# phrase = input("Ingrese una frase: ")

# # Llamar a la función y mostrar el diccionario resultante
# result = create_dictionary_words(phrase)
# print("Diccionario de palabras y sus longitudes:")
# print(result)

'''13.	Escribir una función que calcule el módulo de un vector.'''

# # Ejemplo de uso
# vector_3D = [3, 4, 5]  # Vector tridimensional [x, y, z]
# module = calc_module(vector_3D)
# print(f"El módulo del vector {vector_3D} es: {module}")

'''14.	Requerir al usuario que ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida.'''

# # Pedir al usuario que ingrese un número entero
# number = int(input("Ingrese un número entero: "))
# if is_prime(number):
#     print(f"{number} es un número primo.")
# else:
#     print(f"{number} no es un número primo.")

'''15.	Escribir un programa que pida números al usuario, motrar el factorial de cada uno y, al finalizar, la cantidad total de números leídos en total. 
Utilizar una o más funciones, según sea necesario.'''

# # Programa principal
# def main():
#     total_numbers = get_numbers()
#     print(f"Total de números ingresados: {total_numbers}")

# main()

'''16.	Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias del dígito en el número, 
utilizando para ello una función que calcule la frecuencia.'''

# # Programa principal
# def main():
#     number = int(input("Ingrese un número entero: "))
#     digit = int(input("Ingrese un dígito: "))
        
#     if 0 <= digit <= 9:
#         frequency = calculator_frequency(number, digit)
#         print(f"El dígito {digit} aparece {frequency} veces en el número {number}.")
#     else:
#         print("Por favor, ingrese un dígito válido (0-9).")

# main()

'''17.	Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo. Por cada número, mostrar la suma de sus dígitos. 
También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia). Al finalizar el programa, 
mostrar el factorial del mayor número ingresado.'''

# # Programa principal
# def main():
#     number_prime = True
#     major_prime = 0
    
#     while number_prime:
#         number = int(input("Ingrese un número primo (o un número no primo para salir): "))
#         if number <= 1:
#             number_prime = False
#             break
#         for i in range(2, int(number**0.5) + 1):
#             if number % i == 0:
#                 number_prime = False
#                 break
#         if number:
#             sum_digit_number = sum_digit(number)
#             print(f"Suma de los dígitos: {sum_digit_number}")
                
#             digit = int(input("Ingrese un dígito: "))
#             frequency = calculator_frequency(number, digit)
#             print(f"Frecuencia del dígito {digit}: {frequency}")
                
#             if number > major_prime:
#                 major_prime = number

#     if major_prime > 0:
#         factorial_major_prime = calculator_factorial(major_prime)
#         print(f"Factorial del mayor número primo ingresado: {factorial_major_prime}")
#     else:
#         print("No se ingresaron números primos.")

# main()


