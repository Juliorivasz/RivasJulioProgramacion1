'''1. Calcular el perímetro y área de un rectángulo'''
# base = float(input("Ingrese la base del rectángulo: "))
# altura = float(input("Ingrese la altura del rectángulo: "))

# perimetro = 2 * (base + altura)
# area = base * altura

# print("El perímetro del rectángulo es:", perimetro)
# print("El área del rectángulo es:", area)

'''2. Calcular la hipotenusa de un triángulo rectángulo'''
# import math

# cateto1 = float(input("Ingrese la longitud del primer cateto: "))
# cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

# hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

# print("La hipotenusa del triángulo rectángulo es:", hipotenusa)

'''3. Realizar operaciones con dos números'''
# numero1 = float(input("Ingrese el primer número: "))
# numero2 = float(input("Ingrese el segundo número: "))

# suma = numero1 + numero2
# resta = numero1 - numero2
# multiplicacion = numero1 * numero2
# division = numero1 / numero2

# print("Suma:", suma)
# print("Resta:", resta)
# print("Multiplicación:", multiplicacion)
# print("División:", division)

'''4. Convertir grados Fahrenheit a grados Celsius'''
# fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
# celsius = (fahrenheit - 32) * 5/9
# print("La temperatura en grados Celsius es:", celsius)

'''5. ¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?'''
# a) nombre no esta definido 
# solucion: pedir el nombre y guardarla en la variable nombre
# nombre = input("Como te llamas?")

# b) precio necesita convertirse a float
# precio = float(input("precio: "))

# c) solucion: tiene que estar entre comillas 
# print("tu edad es", edad)

# d) solucion: hay que validar edad
# if edad==18:
#   print("tu edad es 18")
# else:
#   print("tu edad no es 18")

'''6.   Calcular la media de tres números pedidos por teclado.'''
# number1 = float(input("introduce primer numero"))
# number2 = float(input("introduce segundo numero"))
# number3 = float(input("introduce tercer numero"))

# average = (number1+number2+number3)/3

'''7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla 
a cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 
16 horas y 40 minutos.'''

# minutes = int(input("introduce la cantidad de minutos"))
# hours = minutes//60
# missing_minutes = minutes % 60
# print(hours,"horas",missing_minutes,"minutos")

'''8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas 
que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y 
comisiones.'''

# base_salary = float(input("Sueldo base: "))
# sale1= float(input("Venta 1: "))
# sale2= float(input("Venta 2: "))
# sale3= float(input("Venta 3: "))
# sales_commission1 = 0.10 * sale1
# sales_commission2 = 0.10 * sale2
# sales_commission3 = 0.10 * sale3
# total_commissions = sales_commission1+sales_commission2+sales_commission3
# total_sales = base_salary+total_commissions

'''9.	Una tienda ofrece un descuento del 15% sobre el total de la compra y un 
cliente desea saber cuanto deberá pagar finalmente por su compra.'''

# total_purchase= float(input("Monto total de la compra: "))
# buy_discount = round(total_purchase*1.15)
# print("monto total a pagar con descuento: ", buy_discount)

'''10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes:
•	    55% del promedio de sus tres calificaciones parciales.
•	    30% de la calificación del examen final.
•	    15% de la calificación de un trabajo final.
'''

# partial1 = float(input("introduce la calificacion del parcial 1")) 
# partial2 = float(input("introduce la calificacion del parcial 2")) 
# partial3 = float(input("introduce la calificacion del parcial 3"))
# partial_average = round((partial1+partial2+partial3)/3)
# part_1_final_note = partial_average*0.55

# final_exam = float(input("introduce la calificacion del examen final"))
# part_2_final_note = final_exam*0.30

# final_work = float(input("introduce la calificacion del trabajo final"))
# part_3_final_note = final_work*0.15

# final_note = part_1_final_note+part_2_final_note+part_3_final_note

# print("La calificacion final de algoritmos es: ", final_note)

'''11.	Pide al usuario dos números y muestra la “distancia” entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).'''

# number1 = float(input("ingrese el primer numero: "))
# number2 = float(input("ingrese el segundo numero: "))

# distancia = abs(number1-number2)

# print("la distancia entre el numero 1: ", number1, " y ", "numero 2: ", number2, " es: ", distancia)

'''12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada y su raíz cúbica.'''

# number = int(input("introduce un numero entero: "))

# raiz_cubica= number**(1/3)
# raiz_cuadrada= number**(1/2)

# print("la raiz cubica es: ", raiz_cubica, "y la raiz cuadra es: ", raiz_cuadrada)

'''13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número 
invertido. Ejemplo, si se introduce 23 que muestre 32.'''

# number = int(input("introduce un numero: "))
# units = number % 10
# tens = number // 10
# invert_number = units*10+tens
# print(invert_number)

'''14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, 
se pide realizar un algoritmo que intercambie los valores de ambas variables y muestre 
cuanto valen al final las dos variables.'''

# A = int(input("introduce valor de A: "))
# B = int(input("introduce valor de B: "))

# safe = A
# A = B
# B = save
# print("el valor de A es: ", A, "y el de B es: ", B)

'''15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. Escribir un algoritmo 
que determine la hora de llegada a la ciudad B.'''

# HH = int(input("Ingrese la hora de partida (en horas): "))
# MM = int(input("Ingrese los minutos de partida: "))
# SS = int(input("Ingrese los segundos de partida: "))
# T = int(input("Ingrese el tiempo de viaje (en segundos): "))

# horas_viaje = T // 3600
# minutos_viaje = (T % 3600) // 60
# segundos_viaje = (T % 3600) % 60

# HH_llegada = HH + horas_viaje
# MM_llegada = MM + minutos_viaje
# SS_llegada = SS + segundos_viaje

# if SS_llegada >= 60:
#     MM_llegada += 1
#     SS_llegada -= 60

# if MM_llegada >= 60:
#     HH_llegada += 1
#     MM_llegada -= 60

# print("Hora de llegada:", HH_llegada, "horas", MM_llegada, "minutos", SS_llegada, "segundos")

'''16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.'''

# name=input("Introduce tu nombre: ")
# lastname1=input("Introduce tu primer apellido: ")
# lastname2=input("Introduce tu segundo apellido: ")

# initial = name[0]+lastname1[0]+lastname2[0]
# print("tus iniciales son: ", initial)

'''17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una 
variable llamada usuario. A continuación mostrar por pantalla: “Ahora estás en la matrix, 
[nombre del usuario]”.'''

# usuario = input("ingresa tu nombre: ")
# print('"Ahora estas en la matrix,',usuario,'"')

'''18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. 
A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. Imprimir en 
pantalla el monto final a pagar.'''

# dinner_price = float(input("Cuanto costo la cena: "))
# services= dinner_price*0.062
# propine = dinner_price*0.10
# total = dinner_price+services+propine
# print("el precio total de la cena es: ", total)

'''19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar 
cada uno de ellos en una variable numérica (en total, tres variables diferentes). 
Finalmente, mostrar la fecha en formato dd/mm/aaaa.'''

# day=int(input("introduce el DD de tu nacimiento: "))
# month=int(input("introduce el MM de tu nacimiento: "))
# year=int(input("introduce el AAAA de tu nacimiento: "))

# print(day,"/",month,"/",year)

'''20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única 
variable con formato DDMMAAA.'''

# dia = int(input("Ingrese el día de su nacimiento: "))
# mes = int(input("Ingrese el mes de su nacimiento: "))
# anio = int(input("Ingrese el año de su nacimiento: "))

# fecha_nacimiento = "{:02d}{:02d}{:04d}".format(dia, mes, anio)

# print("Fecha de nacimiento: " + fecha_nacimiento)


