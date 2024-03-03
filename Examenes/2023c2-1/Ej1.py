# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un
# mínimo Vertex Cover del mismo.

# Backtracking
def vertex_cover(grafo):
    solucion = []
    minimo = [0] * len(grafo)
    vertex_cover_backtracking(grafo, solucion, minimo)
    return minimo

def es_solucion(grafo, solucion):
    for arista in grafo.aristas:
        if arista[0] not in solucion and arista[1] not in solucion:
            return False
    return True

def vertex_cover_backtracking(grafo, solucion, minimo):
    if len(solucion) >= len(minimo):
        return minimo

    if es_solucion(grafo, solucion):
        return solucion

    for nodo in grafo:
        if nodo not in solucion:
            solucion.append(nodo)
            minimo = vertex_cover_backtracking(grafo, solucion, minimo)
            solucion.pop()
    return minimo

# Este codigo es O(2^n) en el peor caso, ya que por cada nodo tengo dos opciones, estar o no estar en el vertex cover.