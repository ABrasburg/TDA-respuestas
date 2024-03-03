# Somos ayudantes del gran ladrón el Lunático, que está pensando en su próximo atraco. Decidió en este caso robar
# toda una calle en un barrio privado, que tiene la particularidad de ser circular. Gracias a los trabajos de inteligencia
# realizados, sabemos cuánto se puede obtener por robar en cada casa. Podemos enumerar a la primer casa como la casa
# 0, de la cual podríamos obtener g0, la casa a su derecha es la 1, que nos daría g1, y así hasta llegar a la casa n −1, que
# nos daría gn−1. Como la calle es circular, la casa 0 y la n −1 son vecinas. El problema con el que cuenta el Lunático
# es que sabe de experiencias anteriores que, si roba en una casa, los vecinos directos se enterarían muy rápido. No le
# daría tiempo a luego intentar robarles a ellos. Es decir, para robar una casa debe prescindir de robarle a sus vecinos
# directos. El Lunático nos encarga saber cuáles casas debería atracar y cuál sería la ganancia máxima obtenible. Dado
# que nosotros nos llevamos un porcentaje de dicha ganancia, vamos a buscar el óptimo a este problema. Implementar un
# algoritmo que, por programación dinámica, obtenga la ganancia óptima, así como cuáles casas habría que robar, a
# partir de recibir un arreglo de las ganancias obtenibles. Para esto, escribir y describir la ecuación de recurrencia que
# correspondiente. Indicar y justificar la complejidad del algoritmo propuesto.

# Lo resuelvo dos veces, una sin la casa 0 y otra sin la casa n - 1, y me quedo con la mejor solución.
# La ecuación de recurrencia para cada caso es:
# dp[i] = max(dp[i - 1], dp[i - 2] + g[i])

# Es muy parecido a Juan el vago
def max_ganancia(g):
    n = len(g)
    dp = [0] * n
    dp[0] = g[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + g[i])
    maximo = dp[n - 1]
    dp = [0] * n
    dp[1] = g[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + g[i])
    return max(maximo, dp[n - 1])

def robo(g):
    sin_0 = max_ganancia(g[1:])
    sin_n_1 = max_ganancia(g[:-1])
    return max(sin_0, sin_n_1)

print(robo([1, 2, 3, 1])) # 4
print(robo([4, 2, 3, 5])) # 4

# La complejidad del algoritmo es O(n) ya que recorre el arreglo una vez para cada caso.