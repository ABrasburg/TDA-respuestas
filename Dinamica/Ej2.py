# Dado un Grafo dirigido, acíclico G(V, E) con pesos en sus aristas y dos vértices “s” y “t”; queremos encontrar el camino
# de mayor peso que exista entre “s” y “t”. Resolver mediante programación dinámica

def max_path(graph, start, end):
    '''Encuentra el camino de mayor peso entre start y end en el grafo'''
    # Inicializo el arreglo de distancias
    distances = [float('-inf') for _ in range(len(graph))]
    distances[start] = 0
    # Ordeno el grafo topologicamente
    topological_order = topological_sort(graph)
    # Recorro el grafo topologicamente
    for vertex in topological_order:
        for neighbor, weight in graph[vertex]:
            if distances[neighbor] < distances[vertex] + weight:
                distances[neighbor] = distances[vertex] + weight
    return distances[end]

def topological_sort(graph):
    '''Ordena el grafo topologicamente'''
    visited = [False for _ in range(len(graph))]
    topological_order = []
    for vertex in range(len(graph)):
        if not visited[vertex]:
            dfs(graph, vertex, visited, topological_order)
    return topological_order[::-1]

def dfs(graph, vertex, visited, topological_order):
    '''Recorre el grafo en profundidad y guarda el orden topologico en topological_order'''
    visited[vertex] = True
    for neighbor, _ in graph[vertex]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, topological_order)
    topological_order.append(vertex)