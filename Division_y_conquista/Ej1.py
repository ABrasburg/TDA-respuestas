# Contamos con una lista ordenada de “n” coordenadas satelitales (latitud-longitud)
# que conforman un área con forma poligonal convexa. Queremos mostrar ese sector del mapa con el mayor
# tamaño posible en nuestra pantalla rectangular de la computadora. El programa que muestra el mapa acepta como parámetros
# 2 coordenadas para construir el rectángulo a mostrar: los correspondientes a los límites inferior izquierdo y superior derecho.
# Construya un algoritmo eficiente que resuelva el problema con complejidad O(logn).
# ¿Existe una solución de fuerza bruta que para “n” pequeños sea más eficiente? ¿para qué tamaño de n esto cambia?

# Desarrollo:
def max_area(coordinates): # La unica forma de hacerlo en O(log n) es con busqueda binaria
    # Caso base
    if len(coordinates) == 1:
        return coordinates[0], coordinates[0]

    # Dividimos el problema en dos
    middle = len(coordinates) // 2
    left_coordinates = coordinates[:middle]
    right_coordinates = coordinates[middle:]

    # Resolvemos el problema para cada mitad
    left_lower, left_upper = max_area(left_coordinates)
    right_lower, right_upper = max_area(right_coordinates)

    # Unimos las soluciones
    lower = (min(left_lower[0], right_lower[0]), min(left_lower[1], right_lower[1]))
    upper = (max(left_upper[0], right_upper[0]), max(left_upper[1], right_upper[1]))

    return lower, upper

coordinates = [(1, 5), (4, 10), (22, 4), (5,2)]
print(max_area(coordinates))  # ((1, 2), (22, 10))

# La solución de fuerza bruta sería recorrer todas las combinaciones posibles de coordenadas y calcular el área de cada una.
# Esto tiene una complejidad de O(n^2), por lo que para n pequeños, la solución de fuerza bruta es más eficiente.
# Esto cambia cuando n es grande, ya que la solución de fuerza bruta tiene una complejidad cuadrática, mientras que la solución
# con búsqueda binaria tiene complejidad logarítmica.
# Por lo tanto, para n grande, la solución con búsqueda binaria es más eficiente.