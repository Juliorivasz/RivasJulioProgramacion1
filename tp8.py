'''1.	Escribir una función que reciba un número positivo n y devuelva la cantidad de dígitos que tiene.'''

def get_amount_digit(n):
    if n < 0:
        print("El numero ingresado no es positivo")
        return False
    number_str = str(n)
    count = len(number_str)
    return count

result = get_amount_digit(5863)
print(result)

'''2.	Escribir una función que reciba 2 enteros n y b y devuelva True si n es potencia de b.'''

def is_power(n,b):
    # si "n" es menor que "b", entonces "n" no es potencia de "b"
    if n < b:
        return False
    # entra en el bucle si n es mayor a 1
    while n > 1:
        # si n no es divisible completamente por b, entonces no es una potencia de b
        if n % b != 0:
            return False
        # divide n entre b
        n //= b
    # si n es igual 1 al final, entonces es una potencia de b
    return n == 1

print(is_power(27,3))

'''3.	Escribir una funcion recursiva que reciba como parámetros dos strings a y b, y devuelva una lista con las posiciones en donde se encuentra b dentro de a. '''

# el tercer parametro es por defecto y es la posicion
def is_inside(a,b,pos = 0):
    # condicion de salida si la longitud del primer parametro es menor al del segundo
    if len(a) < len(b):
        return []
    # condicion para encontrar el segundo parametro en el primero
    if a[:len(b)] == b:
        return [pos] + is_inside(a[1:],b,pos + 1)
    else:
        return is_inside(a[1:], b, pos + 1)

# imprime la lista con las posiciones
print(is_inside("hola, tienes tiempo de tirar titeres a la tina?", "ti"))