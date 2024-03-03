# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P , por encima del cual se
# rompen. Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor
# forma de distribuir los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto
# para bolsas con peso máximo 5 y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado
# encuentra siempre la solución óptima? Justificar.

# Ordeno los productos de mayor a menor y voy poniendo en la bolsa hasta que no entre mas, y luego paso a la siguiente
# bolsa. Si no entra en ninguna bolsa, abro una nueva.
# O(n*log(n)) en el peor caso, ya que ordeno los productos y luego recorro la lista de productos.
def bolsas(pesos, P):
    pesos.sort(reverse=True)
    bolsas = []
    n = 0
    for peso in pesos:
        if n == 0 or sum(bolsas[n-1]) + peso > P:
            bolsas.append([peso])
            n += 1
        else:
            bolsas[n-1].append(peso)
    return bolsas

print(bolsas([4, 2, 1, 3], 5)) # [[4, 1], [3, 2], [5]]

# No siempre da la optima porque si tengo [4, 3, 2, 1] y P=5, el algoritmo me da [[4], [3, 2], [1]]