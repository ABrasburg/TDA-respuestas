# Dado un número K, se quiere obtener la mínima cantidad de operaciones para llegar de 0 a K, siendo que las operaciones
# posibles son: (i) aumentar el valor del operando en 1; (ii) duplicar el valor del operando.
# Implementar un algoritmo que, por programación dinámica obtenga la menor cantidad de operaciones a realizar (y
# cómo son dichas operaciones). Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad del algoritmo
# implementado.

# dp[i] = min(dp[i-1] + 1, dp[i//2] + 1)

def min_operations(K):
    dp = [float('inf')] * (K + 1)
    dp[0] = 0

    for i in range(1, K + 1):
        print(i, dp)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)
        dp[i] = min(dp[i], dp[i - 1] + 1)

    # Reconstruir las operaciones realizadas
    operaciones = []
    while K > 0:
        if K % 2 == 0 and dp[K] == dp[K // 2] + 1:
            operaciones.append('Duplicar')
            K //= 2
        else:
            operaciones.append('Sumar 1')
            K -= 1

    return dp[-1], operaciones[::-1]

# Ejemplo de uso:
K = 10
min_cantidad, operaciones = min_operations(K)
print("Cantidad mínima de operaciones:", min_cantidad)
print("Operaciones realizadas:", operaciones)