'''1.	Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.'''

# # imprime el ingreso de las lineas de texto
# print("Ingresar lineas de texto, deja la linea vacia para salir: ")
# # lista para guardar las lineas de texto
# lines = []
# # bucle para el ingreso de lineas
# while True:
#     # ingreso de linea
#     line = input()
#     # condicion para guardar en la lista
#     if line:
#         lines.append(line.upper())
#     else:
#         # finaliza el bucle
#         break

# # imprime el resultado de las lineas
# print("Estas son tus lineas: ")
# for line in lines:
#     print(line)

'''2.	Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones. 
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos
'''
# print("Por favor, ingrese las operaciones. Deje una línea en blanco para terminar.")
# balance = 0
# while True:
#     operation = input().upper()
#     if operation:
#         op_type, amount = operation.split()
#         amount = int(amount)
#         if op_type == 'D':
#             balance += amount
#         elif op_type == 'R':
#             balance -= amount
#     else:
#         break

# print("El saldo final es:")
# print(balance)

'''3.	Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
'''
# print("Por favor, ingrese números mayores que 1. Ingrese cero para terminar.")
# primos = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     if num < 2:
#         continue
#     primo = True
#     for i in range(2, num):
#         if num % i == 0:
#             primo = False
#             break
#     if primo:
#         primos += 1

# print("La cantidad total de números primos ingresados es:")
# print(primos)

'''4.	Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
'''

# inicio = int(input("Por favor, ingrese el año de inicio: "))
# fin = int(input("Por favor, ingrese el año de fin: "))

# print("Los años bisiestos y múltiplos de 10 en ese rango son:")
# for año in range(inicio, fin + 1):
#     if año % 10 == 0:
#         if año % 4 == 0:
#             if año % 100 != 0 or año % 400 == 0:
#                 print(año)

'''5.	Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for. Utiliza la declaración continue para omitir los números impares.'''

# for numero in range(1, 21):
#     if numero % 2 != 0:
#         continue
#     print(numero)

'''6.	Crea una lista de números y utiliza un bucle for para encontrar un número específico. Cuando encuentres el número, usa break para salir del bucle.'''

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# numero_buscado = 5

# for numero in numeros:
#     if numero == numero_buscado:
#         print(f"¡Número {numero_buscado} encontrado!")
#         break

'''7.	Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3). 
Utiliza un bucle while para permitir al usuario seleccionar una opción. Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida).'''

# while True:
#     print("Por favor, elija una opción:\n1. Opción 1\n2. Opción 2\n3. Opción 3\n0. Salir")
#     opcion = input()
#     if opcion == "1":
#         print("Has elegido la opción 1.")
#     elif opcion == "2":
#         print("Has elegido la opción 2.")
#     elif opcion == "3":
#         print("Has elegido la opción 3.")
#     elif opcion == "0":
#         print("Has elegido salir. ¡Chau!")
#         break
#     else:
#         print("Opción no válida. Intenta de nuevo.")
