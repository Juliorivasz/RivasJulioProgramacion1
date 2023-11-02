from funciones_parcial_2 import (validate_Letters,show_matriz,is_mutant)
# matriz dna
dna = []
# contador de filas
count_row = 0
print("Introduce 6 filas de adn: ")
# bucle para pedir las filas
while True:
    if count_row == 6:
        break
    # ingresa las secuencias de adn por fila
    row = input(f"Ingresa la Fila {count_row + 1}: ").upper()
    # valida que la letra este permitida
    if not(validate_Letters(row)):
        print("Haz introducido una letra no valida. vuelve a intentarlo")
        continue
    # aumenta el contador de filas
    count_row +=1
    # almacena la fila en la matriz
    dna.append(row)

# muestra la matriz
print("\n ESTA ES LA MATRIZ DE ADN: ")
show_matriz(dna)

# valida si el adn es mutante o no
if is_mutant(dna):
    print("Es Mutante")
else: 
    print("No es Mutante")

# para probar distintos casos de adn
# ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"],  # Secuencia mutante vertical
# ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CGTCTA", "TCACTG"],  # Secuencia mutante en diagonal invertida
# ["ATGCGA", "CAGTGC", "TTGTGT", "AGGTGG", "CGTGTA", "TCACTG"],  # Secuencia mutante en diagonal
# ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"],  # Secuencia mutante oblicua
# ["atgcga", "cagtgc", "ttatgt", "agaagg", "ccccta", "tcactg"],  # Secuencia mutante con letras en minúsculas