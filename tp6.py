'''1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.'''
numbers_list = []
while True:
    numbers = int(input("Ingresa el numero a guardar y 0 para salir: "))
    if numbers == 0:
        break
    numbers_list.append(numbers)

for number in numbers_list:
    print(f"Estos son los numeros que guardaste: {number}")


'''2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.'''
print(f"lista de numeros guardados: {numbers_list}")
while True:
    if len(numbers_list) == 0 or number == 0:
        break
    number = int(input("Ingresa un numero y 0 para salir: "))
    if number in numbers_list:
        numbers_list.remove(number)
        print(f"La primera ocurrencia del número {number} ha sido eliminada.")
        print("La nueva lista es:", numbers_list)
    else:
        print(f"El número {number} no está en la lista. No se puede eliminar.")

'''3.	Imprimir la sumatoria de todos los números de la lista.'''
print(f"lista de numeros guardados: {numbers_list}")
sum_number_total = 0
for number in numbers_list:
    sum_number_total += number

print(f"La suma de los numeros en las lista es: {sum_number_total}")