# Sea C el conjunto de ejes seleccionados por el algoritmo de Dijkstra para un grafo G=(V,E) pesado no dirigido. 
# Probar o dar un contraejemplo las siguientes afirmaciones:
#   a. C corresponde a un árbol recubridor
#   b. C corresponde a un árbol recubridor mínimo.

# a. Falso. Dijkstra no garantiza que el conjunto de ejes seleccionados corresponda a un árbol recubridor. Dijkstra es un
# algoritmo para encontrar el camino más corto entre un nodo origen y todos los demás nodos. No garantiza que el conjunto de
# ejes seleccionados forme un árbol recubridor. Por ejemplo, si el grafo es un ciclo, Dijkstra seleccionará todos los ejes
# del ciclo, pero no formará un árbol recubridor.

# b. Falso. Dijkstra no garantiza que el conjunto de ejes seleccionados corresponda a un árbol recubridor mínimo. Dijkstra
# selecciona los ejes que forman el camino más corto entre un nodo origen y todos los demás nodos. No garantiza que el conjunto
# de ejes seleccionados forme un árbol recubridor mínimo. Por ejemplo, si el grafo es un ciclo, Dijkstra seleccionará todos
# los ejes del ciclo, pero no formará un árbol recubridor mínimo.