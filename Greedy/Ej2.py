# Conocemos al algoritmo de Kruskal y Prim sobre un grafo conexo y ponderado para  obtener su árbol recubridor mínimo. 
# Analice la siguiente estrategia de resolución y determine si corresponde a un algoritmo óptimo. Si lo es, detalle con qué
# estructuras lo implementaría de la forma más eficiente posible.

# Iniciar con el grafo completo
# Mientras existan ciclos en el grafo
#   Obtener la arista de mayor peso cuya remoción mantenga la conectividad del grafo
#   Eliminar la arista seleccionada.

# La estrategia planteada corresponde a un algoritmo de Kruskal. La complejidad de Kruskal es O(E log E) donde E es la cantidad
# de aristas. La complejidad de la estrategia planteada es O(E^2) ya que en el peor caso, se recorren todas las aristas para
# obtener la de mayor peso. En cuanto a la solución, es óptima ya que Kruskal es un algoritmo que garantiza la obtención de
# un árbol recubridor mínimo. La estructura que utilizaría para implementar Kruskal de la forma más eficiente posible es
# un heap binario para obtener la arista de mayor peso en O(log E) y un conjunto disjunto para verificar la conectividad en
# O(1).