# Sea G un grafo dirigido “camino” (las aristas son de la forma (vi, vi+1)). Cada vertice tiene un valor (positivo).
# Implementar un algoritmo que, utilizando programación dinámica, obtenga el Set Independiente de suma máxima
# dentro de un grafo de dichas características. Indicar y justificar la complejidad del algoritmo implementado.

# Es muy parecido a Juan el vago, ya que el independent set de una ilera de nodos es lo mismo que buscar que no haya
# dos dias consecutivos donde se trabaje

def independent_set_max_sum(G):
    n = len(G)
    dp = [0] * n
    dp[0] = G[0]
    dp[1] = max(G[0], G[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + G[i])
    return construccion_de_respuesta(G, dp)

def construccion_de_respuesta(G, dp):
    n = len(G)
    i = n - 1
    res = []
    while i >= 0:
        if i == 0:
            res.append(G[i])
            break
        if i == 1:
            if dp[i] == G[i]:
                res.append(G[i])
            break
        if dp[i] == dp[i-1]:
            i -= 1
        else:
            res.append(G[i])
            i -= 2
    return res

G = [1, 3, 2, 4, 5]
print(independent_set_max_sum(G)) # 9