# Dado “L” un listado ordenado de “n” elementos y un elemento “e” determinado. Deseamos conocer la cantidad total de
# veces que “e” se encuentra en “L”. Podemos hacerlo en tiempo O(n) por fuerza bruta. Presentar una solución utilizando
# división y conquista que mejore esta complejidad.

def buscar_numero(L, e):
    return _buscar_numero(L, e, 0, len(L))

def _buscar_numero(L, e, inicio, fin): # O(log n)
    if inicio == fin:
        return 0
    if inicio+1 == fin:
        return 1 if L[inicio] == e else 0
    medio = (inicio+fin)//2
    return _buscar_numero(L, e, inicio, medio) + _buscar_numero(L, e, medio, fin)

print(buscar_numero([1, 2, 2, 3, 3, 3, 4, 4, 4], 4)) # 3