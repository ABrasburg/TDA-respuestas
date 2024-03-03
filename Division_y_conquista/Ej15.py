# Una encuesta de internet pidió a personas que ordenen un conjunto de “n” películas comenzando por las que más les gusta
# a las que menos. Con los resultados quieren encontrar quienes comparten gustos entre sí. Nos solicitan generar un
# algoritmo, que basándose en el concepto de inversión, compare entre pares de personas y determine qué tan compatibles
# o incompatibles son. Proponer un algoritmo utilizando división y conquista que lo resuelva.

# La inversión es un par de elementos en un arreglo que están en el orden equivocado. Por ejemplo, en el arreglo [2, 4, 1, 3, 5]
# las inversiones son (2, 1) y (4, 1). La cantidad de inversiones en un arreglo ordenado es 0. La cantidad de inversiones en un
# arreglo ordenado de forma descendente es el máximo posible, es decir, (n-1) + (n-2) + ... + 1 + 0 = n*(n-1)/2. La cantidad de
# inversiones en un arreglo desordenado es un indicador de qué tan lejos está de estar ordenado.

def contar_inversiones(peliculas, inicio, fin):
    if inicio >= fin:
        return 0
    
    mitad = (inicio + fin) // 2
    inversiones_izquierda = contar_inversiones(peliculas, inicio, mitad)
    inversiones_derecha = contar_inversiones(peliculas, mitad + 1, fin)
    inversiones_merge = merge_contar_inversiones(peliculas, inicio, mitad, fin)
    
    return inversiones_izquierda + inversiones_derecha + inversiones_merge

def merge_contar_inversiones(peliculas, inicio, mitad, fin):
    inversiones = 0
    izquierda = peliculas[inicio:mitad + 1]
    derecha = peliculas[mitad + 1:fin + 1]
    i = j = 0
    k = inicio
    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            peliculas[k] = izquierda[i]
            i += 1
        else:
            peliculas[k] = derecha[j]
            j += 1
            inversiones += (mitad + 1) - (inicio + i)
        k += 1

    while i < len(izquierda):
        peliculas[k] = izquierda[i]
        i += 1
        k += 1

    while j < len(derecha):
        peliculas[k] = derecha[j]
        j += 1
        k += 1

    return inversiones

def comparar_compatibilidad(personas):
    n = len(personas)
    compatibilidad = []

    for i in range(n):
        for j in range(i + 1, n):
            inversiones = contar_inversiones(personas[i], 0, len(personas[i]) - 1) + contar_inversiones(personas[j], 0, len(personas[j]) - 1)
            compatibilidad.append((i, j, inversiones))

    return compatibilidad

# Ejemplo de uso
personas = [
    ['Pulp Fiction', 'Inception', 'The Dark Knight', 'Fight Club'],
    ['Inception', 'The Dark Knight', 'Fight Club', 'Pulp Fiction'],
    ['The Dark Knight', 'Inception', 'Pulp Fiction', 'Fight Club']
]
resultado = comparar_compatibilidad(personas)
print("Nivel de compatibilidad o incompatibilidad entre personas:")
for a, b, inversiones in resultado:
    print(f"Persona {a} y Persona {b}: {inversiones} inversiones")
