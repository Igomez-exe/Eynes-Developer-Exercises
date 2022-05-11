import random

# Decidí que las listas tengan un rango bajo de numeros aleatorios así es
# más facil obtener los numeros repetidos de forma horizontal y vertical.
def crear_lista():
    aleatorios = [random.randint(0,4) for _ in range(5)]
    return aleatorios

# Se crea la matriz.
m5_5 = [crear_lista(), 
    crear_lista(), 
    crear_lista(),
    crear_lista(),
    crear_lista()]


# Los aux no son numeros enteros, por eso esa asignación.
# ayuda a comparar los elementos de adentro de la matriz.
aux_horizontal = 1.5
aux_vertical = 1.5
i = 0

# La logica es la siguiente, puesto que es una matriz 5 x 5, si los del medio no son 
# iguales, entonces nunca habrá secuencia de cuatro numeros consecutivos.
while i < 5:
    if (m5_5[i][1] ==  m5_5[i][2] == m5_5[i][3]):
        aux_horizontal = m5_5[i][2]

        if aux_horizontal == m5_5[i][0]:
            print("Horizontal: ")
            print("Posicion primer numero: ", (0,i))
            print("Posicion ultimo numero: ", (3,i))
            
        elif aux_horizontal == m5_5[i][4]:
            print("Horizontal: ")
            print("Posicion primer numero: ", (1,i))
            print("Posicion ultimo numero: ", (4,i))


    if(m5_5[1][i] == m5_5[2][i] == m5_5[3][i]):
        aux_vertical = m5_5[2][i]

        if aux_vertical == m5_5[0][i]:
            print("Vertical: ")
            print("Posicion primer numero: ", (i,0))
            print("Posicion ultimo numero: ", (i,3))

        elif aux_vertical == m5_5[4][i]:
            print("Vertical: ")
            print("Posicion primer numero: ", (i,1))
            print("Posicion ultimo numero: ", (i,4))


    i = i + 1

print("")
print(m5_5)