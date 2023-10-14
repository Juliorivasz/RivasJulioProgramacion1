'''20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.'''
# number = int(input("Ingresa un numero entero, presione 0 para salir: "))
# count = number
# while number:
#     number = int(input("Ingresa otro numero entero, presione 0 para salir: "))
#     count += number
# print(f"la suma de los numeros enteros ingresados es {count}")

'''21-	Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.'''

# number = abs(int(input("Ingresa un numero entero positivo, presione 0 para salir: ")))
# major = number
# while number:
#     number = abs(int(input("Ingresa otro numero entero positivo, presione 0 para salir: ")))
#     if(major < number):
#         major = number
# print(f"el numero mayor es {major}")

'''22-	Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. 
La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.'''

# # ingresa el primer numero
# number = int(input("Ingresa un numero entero positivo, presione -1 para salir: "))
# # contador de pares
# count_pair = 0
# while number != -1:
#     # valida que los numeros no sean negativos
#     if number < 0:
#         print("El numero ingresado no es valido, por favor: ")
#     number_str = str(number)
#     # hace la suma de los digitos
#     sum_number = 0
#     for i in number_str:
#         number_int = int(i)
#         sum_number += number_int
#     # encuentra numeros pares
#     if number % 2 == 0:
#         count_pair += 1
#     print(f"la suma de los digitos del numero introducido es: {sum_number}")
#     number = int(input("Ingresa otro numero entero positivo, presione -1 para salir: "))
# print(f"la cantidad de pares son {count_pair}")

'''23-	Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, 
la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.'''

# amount_buys = []
# amount = float(input("introduce el monto de la compra realizada, ingrese 0 para salir: "))

# while amount:
#     amount_buys.append(amount)
#     amount = float(input("introduce el monto de otra compra realizada, ingrese 0 para salir: "))
# print(f"los montos de las compras son: {amount_buys}")

'''24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, 
si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.'''

# amount_pay = float(input("Ingrese el monto a pagar: "))

# while amount_pay < 0:
#     amount_pay = float(input("Ingrese un nuevo monto a pagar: "))

# if amount_pay > 1000:
#     price_off = amount_pay - (amount_pay*0.10)
#     print(f"El monto a pagar seria: ${price_off}")
# else:
#     print(f"El monto a pagar seria: ${amount_pay}")

'''25-	Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. 
El factorial de 0 es 1.'''

# numero = int(input("Ingrese un número entero positivo: "))

# factorial = 1

# if numero < 0:
#     print("El factorial no está definido para números negativos.")
# elif numero == 0:
#     print("El factorial de 0 es 1.")
# else:
#     for i in range(1, numero + 1):
#         factorial *= i

#     print(f"El factorial de {numero} es: {factorial}")
