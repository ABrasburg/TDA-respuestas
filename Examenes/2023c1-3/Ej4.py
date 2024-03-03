# Carlos tiene un problema: sus 5 hijos no se soportan. Esto es a tal punto, que ni siquiera están dispuestos a caminar
# juntos para ir a la escuela. Incluso más: ¡tampoco quieren pasar por una cuadra por la que haya pasado alguno de sus
# hermanos! Sólo aceptan pasar por las esquinas, si es que algún otro pasó por allí. Por suerte, tanto la casa como la
# escuela quedan en esquinas, pero no está seguro si es posible enviar a sus 5 hijos a la misma escuela. Utilizando lo visto
# en la materia, formular este problema y resolverlo. Indicar y justificar la complejidad del algoritmo

# Este es un problema de flujo donde las esquinas son los nodos y las calles son las aristas.
# todas las aristas tienen capacidad 1 y se puede resolver si el flujo máximo es igual o mayor a 5.

def ej4(cant_esquinas, cant_calles, calles):
    # Creo el grafo con las esquinas y las calles
    grafo = {}
    for i in range(cant_esquinas):
        grafo[i] = []
    for calle in calles:
        grafo[calle[0]].append(calle[1])
        grafo[calle[1]].append(calle[0])

    # Creo el grafo de flujo
    grafo_flujo = {}
    for i in range(cant_esquinas):
        grafo_flujo[i] = {}
        for j in grafo[i]:
            grafo_flujo[i][j] = 1

    # Calculo el flujo máximo
    flujo_maximo = ford_fulkerson(grafo_flujo, 0, cant_esquinas-1)

    # Devuelvo si es posible enviar a los 5 hijos a la misma escuela
    return flujo_maximo >= 5