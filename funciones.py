import math
'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos.'''
#Sumar digitos de un numero ingresado.
def sum_digit(number):
    summary=0
    while number>10:
        summary += number%10
        number//=10
    summary += number
    return summary

'''El juego debe mostrar el estado actual de la palabra oculta con guiones bajos (_) que
representan las letras no adivinadas y las letras adivinadas deben mostrarse en su
lugar correspondiente.'''

# encuentra la palabra oculta
def choiced_word(word,phrase):
    characters = ""
    for i in word:
        if i in phrase.lower():
            characters += i
        else:
            characters += "_"
    return characters

# identificador de socios ejercicio 3 tp5
def create_id_partner(first_name, last_name, dni):
    long_last_name= len(last_name)
    id_partner = first_name+str(long_last_name)+dni[:3]
    return id_partner

# si el primer numero es primo del segundo
def are_prime(num_1,num_2):
    return num_1 % num_2 == 0

# Definición de la función para calcular la temperatura media
def calc_temp_medium(temp_max, temp_min):
    temp_medium = (temp_max + temp_min) / 2
    return temp_medium

# Definición de la función para agregar un espacio adicional tras cada letra
def add_space(text):
    text_with_space = ' '.join(text)
    return text_with_space

# Definición de la función para encontrar el valor máximo y mínimo en una lista
def find_max_min(list):
    if not list:  # Si la lista está vacía, devuelve None para ambos valores
        return None, None
    maxim = max(list)
    minim = min(list)
    return maxim, minim

# Funcion para calcular el area y el perimetro de un circulo
def calculate_circle_area_perimeter(radius):
    area = math.pi * radius**2
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Subrutina para verificar el login
def login(user, password, attemps):
    # Verificar si el nombre de usuario y la contraseña son correctos
    if user == "usuario1" and password == "asdasd":
        return True, attemps
    else:
        attemps += 1
        return False, attemps
    

# Función para aplicar descuentos al carrito de compras
def apply_off(cart,offs):
    price_final = 0
    # Iterar a través del diccionario del carrito y aplicar descuentos
    for product, price in cart.items():
        if product in offs:
            discount = price * (offs[product] / 100)
            price -= discount
        price_final += price
    
    return price_final

# Función que aplica la función dada a cada elemento de la lista y devuelve una nueva lista
def apply_function(function, list):
    resultado = []
    for elemento in list:
        resultado.append(function(elemento))
    return resultado

# Función para crear un diccionario con las palabras y sus longitudes
def create_dictionary_words(phrase):
    words = phrase.split()  # Dividir la frase en palabras
    dictionary_words = {}  # Inicializar un diccionario vacío
    for word in words:
        dictionary_words[word] = len(word)  # Agregar palabra y longitud al diccionario
    return dictionary_words

# Función para calcular el módulo de un vector
def calc_module(vector):
    sum_square = sum(x ** 2 for x in vector)
    module = math.sqrt(sum_square)
    return module

# Función para verificar si un número es primo
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Función para calcular el factorial de un número
def calculator_factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * calculator_factorial(number - 1)

# Función para obtener números del usuario y mostrar su factorial
def get_numbers():
    amount_numbers = 0
    while True:
        number = int(input("Ingrese un número (o -1 para salir): "))
        if number == -1:
            break
        factorial = calculator_factorial(number)
        print(f"El factorial de {number} es {factorial}")
        amount_numbers += 1
    return amount_numbers

# Función para calcular la frecuencia de un dígito en un número
def calculator_frequency(number, digit):
    frequency = 0
    while number > 0:
        if number % 10 == digit:
            frequency += 1
        number //= 10
    return frequency