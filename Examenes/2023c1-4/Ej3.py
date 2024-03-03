# Dado un número n, mostrar la cantidad más económica (con menos términos) de escribirlo como una suma de cuadrados,
# utilizando programación dinámica. Indicar y justificar el orden del algoritmo implementado.
# Aclaración: siempre es posible escribir a ncomo suma de ntérminos de la forma 12, por lo que siempre existe solución.
# Sin embargo, la expresión 10 = 32+ 12es una manera más económica de escribirlo para n= 10, pues sólo tiene dos
# términos. Además, tener en cuenta que no se piden los términos, sino la cantidad mínima de términos cuadráticos
# necesaria.

# Este ejercicio es muy parecido al problema delcambio

def crear_monedas(n):
    monedas = []
    for i in range(1, n):
        if i * i <= n:
            monedas.append(i * i)
        else:
            break
    return monedas

def cantidad_minima(n): # O(n * m) donde m es la cantidad de monedas
    monedas = crear_monedas(n)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        minino = i
        for moneda in monedas:
            if moneda > i:
                break
            if dp[i - moneda] + 1 < minino:
                minino = dp[i - moneda] + 1
        dp[i] = minino
    return dp[n]

print(cantidad_minima(10)) # 2