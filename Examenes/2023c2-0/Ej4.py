# Implementar un algoritmo que reciba un Grafo y un número k y devuelva un dominating set de dicho grafo de a lo
# sumo k vértices

# Backtracking

def set_dominante(grafo, k):
    solucion = []
    adyacentes = []
    total = 0
    for nodo in grafo:
        if nodo not in adyacentes:
            solucion.append(nodo)
            adyacentes.extend(grafo.adyacentes(nodo))
            total += 1
            if total == k:
                break
    nodos = grafo.nodos()
    for nodo in solucion:
        nodos.remove(nodo)
        for nodo2 in grafo.adyacentes(nodo):
            nodos.remove(nodo2)
    if len(nodos) > 0:
        return None
    return solucion

