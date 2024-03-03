# Implementar un algoritmo que, por backtracking, obtenga todos los posibles ordenamientos topológicos de un grafo
# dirigido y acíclico.

def orden_topologico(grafo):
    sol = []
    soluciones = []
    visitados = [False] * len(grafo)
    orden_topologico_backtracking(grafo, sol, soluciones, visitados)
    return soluciones

def orden_topologico_backtracking(grafo, sol, soluciones, visitados):
    if len(sol) == len(grafo):
        # Reviso si cumplen con la condición de ser un orden topológico
        for i in range(len(sol) - 2):
            if grafo.tiene_arista(sol[len(sol)-1], sol[i]):
                return
        soluciones.append(sol)
        return
    for nodo in grafo:
        if not visitados[nodo]:
            # Reviso si cumplen con la condición de ser un orden topológico
            for i in range(len(sol) - 2):
                if grafo.tiene_arista(sol[len(sol)-1], sol[i]):
                    continue
            visitados[nodo] = True
            sol.append(nodo)
            orden_topologico_backtracking(grafo, sol, soluciones, visitados)
            sol.pop()
            visitados[nodo] = False