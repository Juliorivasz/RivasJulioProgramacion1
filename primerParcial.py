# diccionario de vocales
vocal = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# pide el nombre al usuario
name = input("Ingresa tu nombre, por favor: ").capitalize()

# muestra las opciones
print(f"{name}, los juegos a elegir son: ")
print(f"1. Juego de numeros")
print(f"2. Juego de palabras")

# selecciona la opcion a jugar
pick_option = int(input(f"{name}, elige una opcion 1 o 2: "))

# valida que solo introduzca una de las opciones disponibles
while pick_option != 1 and pick_option != 2:
    pick_option = int(input(f"{name} haz introducido una opcion no valida, vuelve a elegir una opcion: "))

# valida la opcion 1
if pick_option == 1:
    # introduce el numero entero
    number_int = int(input(f"{name}, introduce un numero entero: y para salir introduce 0: "))
    # guarda el numero par mayor
    major = 0
    # suma de todos los impares
    odd_sum = 0
    # cantidad de impares
    count = 0
    # bucle para que te siga pidiendo un numero entero hasta introducir 0
    while number_int:
        # encuentra el numero mayor que sea par
        if number_int > major and number_int % 2 == 0:
            major = number_int
        # valida cantidad de impares y los suma en odd_sum para sacar el promedio
        elif number_int % 2 == 1:
            odd_sum += number_int
            count +=1
        number_int = int(input(f"{name}, introduce otro numero entero: y para salir ingresa 0: "))
    # imprime el numero mayor par y el promedio de los impares
    print(f"El numero mayor par introducido por {name} es: {major}")
    print(f"El promedio de los numeros impares es: {odd_sum/count}")
# valida opcion 2 
elif pick_option == 2:
    # pide la frase
    sentence = input(f"{name}, ingresa una frase: ").lower()
    # contador de las vocales
    count_vocal = 0
    # recorre la cadena
    for k in sentence:
        # valida si la letra se encuentra en la lista vocal
        if k in vocal:
            vocal[k] += 1
            count_vocal +=1
    # Imprimir la cantidad de veces que aparece cada vocal
    for v, cantidad in vocal.items():
        print(f'La vocal {v} aparece {cantidad} veces en el texto.')
    # si no contiene vocales
    if count_vocal == 0:
        print(f"{name}, la frase no contiene vocales")
