# Dado un flujo máximo de un grafo, implementar un algoritmo que, si se le aumenta la capacidad a una artista, permita
# obtener el nuevo flujo máximo en tiempo lineal en vértices y aristas. Indicar y justificar la complejidad del algoritmo
# implementado.

from collections import deque

def bfs(graph, parent, source, sink):
    visited = [False] * len(graph)
    queue = deque()
    queue.append(source)
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v, capacity, flow in graph[u]:
            if not visited[v] and capacity > flow:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return visited[sink]

def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0

    while bfs(graph, parent, source, sink):
        path_flow = float("inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s][0] - graph[parent[s]][s][1])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v][1] += path_flow
            graph[v][u][1] -= path_flow
            v = parent[v]

    return max_flow

# Ejemplo de uso
graph = [
    [[0, 5], [0, 3]],  # Aristas salientes del vértice 0: [(capacidad, flujo), (capacidad, flujo)]
    [[0, 0], [0, 2]],  # Aristas salientes del vértice 1: [(capacidad, flujo), (capacidad, flujo)]
]
source = 0
sink = 1

# Flujo máximo original
max_flow_original = ford_fulkerson(graph, source, sink)
print("Flujo máximo original:", max_flow_original)

# Aumento la capacidad de una arista
graph[0][1][0] += 1  # Aumento la capacidad de la arista (0, 1) en 1

# Nuevo flujo máximo después del aumento
new_max_flow = ford_fulkerson(graph, source, sink)
print("Nuevo flujo máximo después del aumento:", new_max_flow)