# Carlitos (primo de Juan, el vago) trabaja para una empresa de publicidad. Tiene un determinado presupuesto P que no
# puede sobrepasar, y tiene que una serie de campañas publicitarias para elegir. La campaña i cuesta $Ci. También se
# han realizado diversos estudios que permiten estimar cuánta ganancia nos dará cada campaña, que denominaremos Gi.
# Implementar un algoritmo que reciba esta información y devuelva cuáles campañas debe realizar Carlitos. Indicar y
# justificar la complejidad del algoritmo propuesto. ¿Da lo mismo si los valores están expresados en pesos argentinos,
# dólares u otra moneda? (haciendo la equivalencia de divisa, siempre suponiendo valores enteros).

# Lo resuelvo como el problema de la mochila con una matriz de n x P, donde n es la cantidad de campañas y P el presupuesto
# la ecuacion de recurrencia es:
# dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - Ci] + Gi)
# Asumiendo que desde un principio puedo hacer cualquier campaña

def crear_matriz(n, m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(0)
    return matriz

def publicidad(C, G, P):
    matriz = crear_matriz(len(C)+1, P)
    # Lleno la columna donde no hay proyecto con P ya que no puedo hacer nada
    for i in range(len(C)+1):
        matriz[0][i] = i+1
    for i in range(1, len(C)+1):
        for j in range(P):
            print( "IF",matriz[i-1][j], C[i - 1])
            if matriz[i-1][j] >= C[i - 1]:
                print(matriz[i-1][j], matriz[i - 1][j - C[i - 1]],"C",C[i-1],"G", G[i - 1])
                matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - C[i - 1]] - C[i-1] + G[i - 1])
                print("QUEDO", matriz[i][j])
            else:
                matriz[i][j] = matriz[i - 1][j]
    print(matriz)
    return matriz[len(C)][P-1]

print(publicidad([4, 2, 3, 4], [5, 3, 4, 5], 5)) # [3, 2]
# No funciona pero se entiende la idea