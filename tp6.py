'''1.	Solicitar al usuario que ingrese números, estos deben guardarse en una lista. Para finalizar el usuario debe ingresar 0, el cual no debe guardarse.'''
# numbers_list = []
# while True:
#     numbers = int(input("Ingresa el numero a guardar: "))
#     if numbers == 0:
#         break
#     numbers_list.append(numbers)

# for number in numbers_list:
#     print(f"Estos son los numeros que guardaste: {number}")


'''2.	A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista, eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.'''
# number_list = [4,8,3,5,23]
# while True:
#     number = int(input("Ingresa un numero: "))
#     if number in number_list:
#         number_list.remove(number)
#         print(f"La primera ocurrencia del número {number} ha sido eliminada.")
#         print("Lanueva lista es:", number_list)
#     else:
#         print(f"El número {number} no está en la lista. No se puede eliminar.")