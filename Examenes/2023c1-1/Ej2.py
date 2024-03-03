# Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
# Implementar un algoritmo que dé la cantidad mínima de faros que se necesitan para que todos los submarinos queden
# iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las diagonales), y las
# directamente adyacentes a estas (es decir, un “radio de 2 celdas”)

# Hago fuerza bruta
# O(n*m) en el peor caso, ya que recorro la matriz y para cada celda, si no tiene faro, pongo uno y pongo faros en las
def faros(matriz):
    n = len(matriz)
    m = len(matriz[0])
    faros = 0
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == 1:
                faros += 1
                for x in range(i-2, i+3):
                    for y in range(j-2, j+3):
                        if x >= 0 and x < n and y >= 0 and y < m:
                            matriz[x][y] = 0
    return faros

matriz = [
    [1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1]
]
print(faros(matriz)) # 4