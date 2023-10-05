# 1. Crea una variable llamada "numero1" y asígnale un número entero de tu elección.
numero1 = 10

# 2. No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal de tu elección.
numero2 = 5.5

# 3. Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2".
suma = numero1 + numero2

# 4. Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para multiplicación y otra para división.
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

# 5. Crea una variable llamada "nombre" y asígnale tu nombre como valor.
nombre = "Julio"

# 6. Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio.
precio = 50.75

# 7. Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale un valor decimal que represente el descuento aplicado al artículo.
descuento = 0.25

# 8. Calcula el precio final aplicando el descuento al precio original y almacena el resultado en una variable llamada "precio_final".
precio_final = precio - (precio * descuento)

# 9. Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu elección. Qué sea un string.
cadena = "Hola, mundo."

# 10. Sin borrar la variable "cadena", crea una nueva variable llamada "longitud" y almacena la longitud en caracteres de la cadena utilizando una de las funciones de Python.
longitud = len(cadena)

# 11. Convierte la variable "precio" en número entero.
precio = int(precio)

# 12. Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas en una tercera variable llamada "nombre_completo".
nombre = "Julio"
apellido = "Rivas"
nombre_completo = nombre + " " + apellido

# 13. Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.
edad = 25
edad += 5
edad -= 10

# 14. Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y centímetros. Multiplícala por 4 y luego divídela en 3.
altura = 1.83
altura = (altura * 4) / 3

# 15. Crea una variable que contenga tu nombre completamente en mayúsculas. Después transfórmalo todo en minúsculas con algún método o función de Python.
nombre_mayusculas = nombre_completo.upper()
nombre_minusculas = nombre_mayusculas.lower()

# 16. Con la variable con el nombre en mayúsculas, aplica un método para que se transforme todo en minúsculas excepto la primera letra.
nombre_capitalizado = nombre_mayusculas.capitalize()

# Imprimir los resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("Nombre Completo:", nombre_completo)
print("Precio Final:", precio_final)
print("Longitud de la Cadena:", longitud)
print("Edad:", edad)
print("Altura:", altura)
print("Nombre en Mayúsculas:", nombre_mayusculas)
print("Nombre en Minúsculas:", nombre_minusculas)
print("Nombre Capitalizado:", nombre_capitalizado)
