# Para la elaboración de un juego se desea construir un cielo nocturno de una ciudad donde se vea el contorno de los
# edificios en el horizonte. Cada edificio “ei“ está representado por rectángulos mediante la tripla
# (izquierda, altura, derecha). Dónde “izquierda” corresponde a la coordenada x menor, “derecha” la coordenada x mayor y
# altura la coordenada y. Todos los edificios inician en la coordenada 0 de y. Se cuenta con una lista de N edificios que
# llegan sin un criterio de orden específico. Se desea emitir como resultado el contorno representado como una lista de
# coordenadas “x” y sus alturas.
# Tenga en cuenta el siguiente ejemplo: Lista de edificios: (1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16) ,
# (14, 3, 25), (19,18,22). Contorno: (1,11),(3,13),(9,0),(12,7),(16,3),(19,18),(22,3),(25,0).
# Presentar un algoritmo utilizando división y conquista que dado el listado de edificios retorna como resultado el
# contorno de la ciudad.

def merge(left, right):
    i = j = 0
    sorted_contour = []
    h1 = h2 = 0
    x = 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            x = left[i][0]
            h1 = left[i][1]
            i += 1
        else:
            x = right[j][0]
            h2 = right[j][1]
            j += 1
        max_h = max(h1, h2)
        if not sorted_contour or max_h != sorted_contour[-1][1]:
            # Si la altura máxima es diferente a la última altura en el contorno, se agrega el punto
            sorted_contour.append([x, max_h])
    sorted_contour.extend(left[i:])
    sorted_contour.extend(right[j:])
    print("Sorted contour:", sorted_contour)
    return sorted_contour

def get_contour(buildings):
    if len(buildings) == 1:
        x, h, y = buildings[0]
        return [[x, h], [y, 0]]
    mid = len(buildings) // 2
    left = get_contour(buildings[:mid])
    right = get_contour(buildings[mid:])
    return merge(left, right)

# Ejemplo de uso
buildings = [(1, 11, 5), (2, 6, 7), (3, 13, 9), (12, 7, 16), (14, 3, 25), (19, 18, 22)]
contour = get_contour(buildings)
print("Contorno:", contour)  # Debería imprimir: [[1, 11], [3, 13], [9, 0], [12, 7], [16, 3], [19, 18], [22, 3], [25, 0]]