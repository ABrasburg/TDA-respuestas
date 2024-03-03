# Se cuenta con un vector V de “n” elementos. Este vector visto de forma circular está ordenado. Pero no necesariamente
# en la posición inicial se encuentra el elemento más pequeño. Deseamos conocer la cantidad total de rotaciones que
# presenta “V”. Ejemplo: V = [6, 7, 9, 2, 4, 5] se encuentra rotado en 3 posiciones. Podemos hacerlo en tiempo O(n) por
# fuerza bruta. Presentar una solución utilizando división y conquista que mejore esta complejidad.

# Busco el elemento que es menor que el anterior
def encontrar_rotaciones(vector):
    izquierda, derecha = 0, len(vector) - 1
    return _encontrar_rotaciones(vector, izquierda, derecha)

def _encontrar_rotaciones(vector, izquierda, derecha):
    if izquierda == derecha:
        return izquierda
    medio = (izquierda + derecha) // 2
    if vector[medio] < vector[medio-1]:
        return medio
    izq = _encontrar_rotaciones(vector, izquierda, medio)
    der = _encontrar_rotaciones(vector, medio+1, derecha)
    if vector[izq] < vector[der]:
        return izq
    return der

# Ejemplo de uso
vector = [6, 7, 9, 10, 2, 4, 5]
rotaciones = encontrar_rotaciones(vector)
print("El número de rotaciones es:", rotaciones)
