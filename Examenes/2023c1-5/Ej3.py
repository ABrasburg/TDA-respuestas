# Dada una soga de n metros (n ≥2) implementar un algoritmo que, utilizando programación dinámica, permita cortarla
# (en partes de largo entero) de manera tal que el producto del largo de cada una de las partes resultantes sea máximo. El
# algoritmo debe devolver el valor del producto máximo alcanzable. Indicar y justificar la complejidad del algoritmo.
# Ejemplos:
# n = 2 --> Debe devolver 1 (producto máximo es 1 * 1)
# n = 3 --> Debe devolver 2 (producto máximo es 2 * 1)
# n = 5 --> Debe devolver 6 (producto máximo es 2 * 3)
# n = 10 -> Debe devolver 36 (producto máximo es 3 * 3 * 4)

# Lo resuelvo como el problema de la mochila, pero en vez de maximizar el valor, maximizo el producto

def max_product(n):
    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        maximo = 0
        for j in range(1, i):
            maximo = max(maximo, j * (i - j), j * dp[i - j])
        dp[i] = maximo
    return dp[n]

print(max_product(2)) # 1
print(max_product(3)) # 2
print(max_product(5)) # 6
print(max_product(10)) # 36