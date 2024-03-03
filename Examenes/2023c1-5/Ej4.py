# Se tiene una matriz donde en cada celda hay submarinos, o no, y se quiere poner faros para iluminarlos a todos.
# Implementar un algoritmo que Greedy que dé la cantidad mínima de faros que se necesitan para que todos los
# submarinos queden iluminados, siendo que cada faro ilumina su celda y además todas las adyacentes (incluyendo las
# diagonales), y las directamente adyacentes a estas (es decir, un “radio de 2 celdas”). Indicar y justificar la complejidad
# del algoritmo implementado. ¿El algoritmo implementado da siempre la solución óptima?

# Lo resuelvo con un algoritmo greedy, donde en cada paso pongo un faro en la celda con más submarinos adyacentes
# teniendo un cuenta un radio de dos que no estén iluminados.

def faros(matriz):
    # Veo que celda tiene más submarinos adyacentes
    faros = 0
    while True:
        print(matriz)
        maximo = 0
        celda = celda_max_submarinos(matriz)
        if celda is None:
            break
        faros += 1
        for i in range(max(0, celda[0] - 2), min(len(matriz), celda[0] + 2)):
            for j in range(max(0, celda[1] - 2), min(len(matriz[0]), celda[1] + 2)):
                if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]):
                    matriz[i][j] = 0
    return faros

# Este codigo no da siempre el mejor