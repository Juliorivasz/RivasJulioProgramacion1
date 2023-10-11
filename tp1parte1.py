'''1.	Indica si los siguientes identificadores son válidos en Python. En el caso de que el identificador no sea válido, explica el motivo.'''

# a) alumno1 => 'es valido'
# b) 1alumno => 'no es valido porque no puede iniciar con un numero'
# c) primerNombre => 'es valido'
# d) /apellido => 'No es valido porque no puede comenzar con caracteres especiales con excepcion del guion bajo'
# e) tamaño_maximo => 'Es valido'
# f) for => 'No es valido, es una palabra reservada'
# g) _$nombre => 'no permite caracteres especiales'
# h) global => 'No es valido, palabra reservada del lenguaje'
# i) primer_nombre => 'Es Valido'
# j) num_mayor => 'es valido'
# k) menor_num => 'es valido'
# l) dni@alumno => 'No es valido tiene caracteres especiales'
# m) 5var => 'No es valido, no se puede iniciar con un numero'
# n) with => 'No es valido es una palabra reservada'
# o) Auto-seleccionado => 'No es valido, tiene caracter especial'
# p) %aumento => 'no es valido, posee caracter especial'
# q) _123 => 'es valido'
# r) ValorTotal => 'es valido'
# s) DESCUENTO => 'es valido'
# t) año => 'es valido'
# u) mes_actual => 'es valido'
# v) apellido&nombre => 'no es valido, tiene caracter especial'
# w) 89GW5 =>  'no es valido, inicia con numero'
# x) valido? => 'no es valido, tiene un caracter especial'

'''2.	Indica qué dato se guarda en la variable x en cada caso, suponiendo una ejecución secuencial del programa.'''
# a) x = 46
# x = 15
# x = 30
# la variable x guarda el valor de 30

# x = 25
# x+10
# la variable x guarda el valor 25

# x = 10-2
# 10+2
# la variable x guarda el valor de 8

# y = 3*(4+2)
# x = y+2
# z = 5
# x = y-z
# la variable x guarda el valor 13

# x = 3
# y = x+6
# x = y-1
# la variable x guarda el valor 8

'''3.	Indica qué tipo de dato se guarda en cada variable.'''

# a) var1 = 100/5 => "entero"
# b) var2 = 7/2 => "flotante"
# c) var3 = 7//2 => "entero"
# d) var4 = 7%2 => "entero"
# e) var5 = 'a' => "string"
# f) var6 = "casa"+"s" => "string"
# g) var7 = "automovil"[1+1] => "string"
# h) var8 = len("carpeta") => "entero"
# i) var9 = int("748") => "entero"
# j) var10 = float("832") => "flotante"
# k) var11 = float(321) => "flotante"
# l) var12 = str(65) => "string"
# m) var13 = 1+5!=3 => "booleano"
# n) var14 = 177%2==0 => "booleano"
# o) var15 = len("ola")<=12 => "booleano"

'''4.	Indica cuáles de las siguientes operaciones no son válidas.'''

# a) 11-(4%2+10) => "valido"
# b) "30"+"2" => "valido"
# c) "30" + 2 => "no es valido"
# d) "hola"[len("hola")] => "no es valido"
# e) len(456) => "no es valido"
# f) "hola"[len("fin")] => "no es valido"
# g) int("4") => "valido"
# h) int(4) => "valido"
# i) int("z") => "no es valido"
# j) int("4.") => "no es valido"
# k) 4<"f" => "no es valido"
# l) "palabra"="rama" => "no es valido"

'''5.	Declara una variable de cada tipo de dato y asígnale un valor.'''

# a) age = 22
# b) balance = 30.5
# c) voltage = 5 + 2j
# d) name = "julio"
# e) older = edad >=18
# f) list_age = [7,10,15,21,27,30]
# g) invited = ("pedro","juan","francisco")
# h) person = {name: "julio", age: 23, profession: "program"}
# i) count = None

'''6.	Teniendo la variable de tipo string: frase = “Caminante, no hay camino, se hace camino al andar.”, indica qué obtendríamos si aplicáramos:'''
# a) frase[5] => "a"
# a) frase[-1] => "r" 
# a) frase[0:8] => "caminant"
# a) frase[::3] => "Cin,oaci,ea molnr"

'''7.	Usando la variable del ejercicio anterior:'''

# a) ¿como obtenemos la cadena al reves? => frase[::-1]
# b) ¿ como obtenemos la subcadena "hace" => frase.split()[5]

'''8.	Métodos upper(), lower() y title().'''

# a) nombre.title()
# b) frase.lower()
# c) frase.upper()

'''9.	Convierte en expresiones algorítmicas las siguientes expresiones algebraicas. Coloca paréntesis solamente donde sean necesarios.'''

# a) expresion1 = (b / 2) - (4 * a * c)
# b) expresion2 = (3 * x * y) - (5 * x) + (12 * x) - 17
# c) expresion3 = (b + d) / (c + 4)
# d) expresion4 = ((x * y) / y) + 2
# e) expresion5 = (1 / y) + ((3 * x) / z) + 1
# f) expresion6 = (1 / (y + 3)) + (x / y) + 1
# g) expresion7 = a**2 + b**2
# h) expresion8 = (a + b)**2
# i) expresion9 = b**(1 / 3) + 34
# j) expresion10 = (x / y) * (z + w) * 3.14
# k) expresion11 = (x + y) / (u + (w / b))

'''10.	Convierte en expresiones algebraicas las siguientes expresiones algorítmicas. Coloca paréntesis solamente donde sean necesarios.'''

# a) x = (-b+(b**2-4*a*c)**(1/2))/(2*a)
# b) (x**2+y**2)/(z**2)
# c) 4*x**2-2*x+7
# d) (b**2)**(1/2)-4*a*c
# e) (a-b)**2+(c-d)**3
# f) (x+y)/y-(3*x)/5
# g) (a**2+b**2)**(1/3)=c
# h) 3*x**2/(3*x**3/(4*y+6))**(1/2)

'''11.	Dada la siguiente expresión aritmética: Determinar qué resultado obtendremos si a=5, b=2, c=6, x=(-6) y y=4.'''

# el resultado es 10*(5/8)

'''12.	Escribe las expresiones algorítmicas equivalentes a los siguientes enunciados:'''

# a) 5+3
# b) (4+7+9)/3
# c) 8*5
# d) n%2
# e) 16*2
# f) (8-3)*6
# g) (2*6)-(4+3)
# h) N%2 == 0 y N%3 == 0
# i) precio >= 15 y precio < 90
# j) N+=12
# k) N-=5
# l) N*=3
# m) N*=1/2

'''13.	¿Qué resultado (True/False) dan las siguientes operaciones?'''

# a) false
# b) true
# c) false
# d) false
# e) false
# f) true
# g) true
# h) true
# i) true

'''14.	Siendo x una variable de tipo entera, con valor 5, determine qué se mostrará por pantalla en cada caso.'''

# a) 6
# b) 3
# c) 25
# d) 1

'''15.	Tipos list, tuple y dict.'''

# a) amarillo
# b) rojo posicion 0 y rosa posicion 7
# c) list = ["tres","dos","cinco","cuatro","uno"]
# d) print(colores[1])
# e) operacion = numeros[0]-numeros[1]+numeros[2]+numeros[3]
# f) len(diccionario)
# g) diccionario["c"]

'''16.	Vamos a practicar el uso de las funciones input() y print().'''

# a) number1 = int(input("introduce primer numero entero: ")) 
# a) number2 = int(input("introduce segundo numero entero: "))
# a) sum = number1+number2
# a) print(suma)

# b) age = int(input("ingresa tu edad: "))
# b) hundred_years = 100 - age
# b) print(hundred_years)

'''17.	Operadores ternarios.'''
# a) number=int(input("introduce un numero: "))
# a) par_impar= "par" if number%2==0 else "impar"

# b) abs(number)

# c) bigger= num1 if num1>num2 else num2

