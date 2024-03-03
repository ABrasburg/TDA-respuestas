# Para una inversión inmobiliaria un grupo inversor desea desarrollar un barrio privado paralelo a la una ruta. Con
# # ese motivo realizaron una evaluación de los diferentes terrenos en un trayecto de la misma. Diferentes inversores
# # participarán, pero a condición de comprar algún terreno en particular. El grupo inversor determinó para cada
# propiedad su evaluación de ganancia. El mismo surge como la suma de inversiones ofrecida por el terreno menos el
# costo de compra. Debemos recomendar que terrenos contiguos comprar para que maximicen sus ganancias.
#  Ejemplo: S = [-2, 3, -3, 4, -1, 2]. La mayor ganancia es de 5, comprando los terrenos de valor  [4, -1, 2].
# Solucionar el problema mediante un algoritmo de programación dinámica.

# O(n)
def terrenos(S):
    matriz_inicio = [[0] * len(S) for _ in range(len(S))]
    matriz_inicio[0][0] = S[0]
    for i in range(1, len(S)):
        for j in range(0, i+1):
            matriz_inicio[i][j] = matriz_inicio[i - 1][j] + S[i]

    maximo = 0
    for j in range(len(S)):
        for i in range(j, len(S)):
            if matriz_inicio[i][j] > maximo:
                maximo = matriz_inicio[i][j]
    print(matriz_inicio)
    return maximo

print(terrenos([-2, 3, -3, 4, -1, 2])) # [4, -1, 2]
