# valida la letra
def validate_Letters(string):
    boolean = True
    letters = ["A","T","C","G"]
    for letter in string:
        # si la letra no esta en las permitidas
        if letter not in letters:
            # retorna false
            boolean =  False
    # si no retorna true
    return boolean

# imprima la matriz
def show_matriz(matriz):
    print("")
    # itera la fila
    for row in matriz:
        # itera cada columna
        for column in row:
            print("",column, "", end=" ")
        print("\n-----------------------")

# valida si es mutante o no
def is_mutant(dna):
    # contador de mas de una secuencia
    count = 0
    for i in range(6):
        # busqueda Horizontal
        count += sequence_dna(dna[i])
        # busqueda vertical
        column= ""
        for j in range(6):
            # concatena las letras verticales
            column += dna[j][i]
        # suma el numero de secuencias encontradas en la cadena
        count += sequence_dna(column)

    # busqueda diagonal (derecha a izquierda)
    for i in range(3):
        for j in range(3):
            diagonal = ""
            for d in range(4):
                # concatena las diagonales (d a i)
                diagonal += dna[i+d][j+d]
            count += sequence_dna(diagonal)

    
    # busqueda diagonal (izquierda a derecha)
    for i in range(3):
        for j in range(3,6):
            diagonal = ""
            for d in range(4):
                #concatena diagonales (i a d)
                diagonal += dna[i+d][j-d]
            count += sequence_dna(diagonal)

    return count > 1

def sequence_dna(sequence):
    # almacena la cantidad de secuencias
    count = 0
    # itera por indice la cadena
    for i in range(len(sequence) - 3):
        # valida que tenga 4 letras consecutivas iguales
        if sequence[i] == sequence[i+1] == sequence[i+2] == sequence[i+3]:
            count +=1
        return count