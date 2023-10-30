'''1.	Escribe un programa que tome una lista de números como entrada y la ordene en orden ascendente utilizando el método de ordenamiento de burbuja.'''

numbers_list = [5,8,2,4,3]
aux = 0
# Iterar todos los elementos de la lista
for number in range(len(numbers_list)):
    # Últimos i elementos ya están ordenados
    for num in range(len(numbers_list)-number-1):
        # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
        if numbers_list[num] > numbers_list[num+1]:
            aux = numbers_list[num]
            numbers_list[num] = numbers_list[num+1]
            numbers_list[num+1] = aux
print("Resultado del ejercicio N° 1")
print(numbers_list)

'''2.	Crea un programa que tome una lista de palabras como entrada y las ordene alfabéticamente en orden ascendente utilizando el método de ordenamiento de selección.'''
word_list = ["python", "programación", "desarrollo", "computadora", "tecnología"]
aux = ""
for i in range(len(word_list)):
        # Encontrar el mínimo en la parte desordenada de la lista
        min_idx = i
        for j in range(i+1, len(word_list)):
            if word_list[j] < word_list[min_idx]:
                min_idx = j
        #  Intercambiar la palabra mínima encontrada con la primera palabra de la parte desordenada
        aux = word_list[i]
        word_list[i] = word_list[min_idx]
        word_list[min_idx] = aux

print("Resultado del ejercicio N° 2")
print(word_list)

'''3.	Crea una lista de diccionarios, donde cada diccionario contiene información sobre un libro (título, autor, año de publicación, etc.). Luego, 
escribe un programa que ordene la lista de libros en función de un campo específico, como el año de publicación o el autor.'''

books_harry_potter = [
    {"titulo": "Harry Potter y la cámara secreta", "autor": "J.K. Rowling", "año_publicacion": 1998},
    {"titulo": "Harry Potter y el prisionero de Azkaban", "autor": "J.K. Rowling", "año_publicacion": 1999},
    {"titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "año_publicacion": 1997},
    {"titulo": "Harry Potter y la Orden del Fénix", "autor": "J.K. Rowling", "año_publicacion": 2003},
    {"titulo": "Harry Potter y el cáliz de fuego", "autor": "J.K. Rowling", "año_publicacion": 2000},
    {"titulo": "Harry Potter y las reliquias de la Muerte", "autor": "J.K. Rowling", "año_publicacion": 2007},
    {"titulo": "Harry Potter y el misterio del príncipe", "autor": "J.K. Rowling", "año_publicacion": 2005}
]

n = len(books_harry_potter)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if books_harry_potter[j]["año_publicacion"] < books_harry_potter[min_idx]["año_publicacion"]:
            min_idx = j
    books_harry_potter[i], books_harry_potter[min_idx] = books_harry_potter[min_idx], books_harry_potter[i]

print("Resultado del ejercicio N° 3")
for book in books_harry_potter:
    print(f"El titulo es: {book["titulo"]}, el autor es: {book["autor"]} y el año de publicacion es: {book["año_publicacion"]}.")
