# Se realiza un experimento de conductividad de un nuevo material en aleación con otro. Se formaron muestras numeradas
# de 1 a n. A mayor número, mayor concentración del nuevo material. Además se realizaron “n” mediciones a diferentes
# temperaturas de conductividad para cada muestra. Los resultados fueron expresados en una matriz M de nxn. Se observa
# que un mismo material cuanto mayor temperatura tiene mayor conductividad. Además, cuanto mayor concentración a la misma
# temperatura, también mayor conductividad. En conclusión podemos, al analizar la matriz, ver dos progresiones. Cada
# fila tiene números ordenados de forma creciente y cada columna tiene números ordenados de forma creciente. Dada la
# matriz M, los experimentadores quieren encontrar en qué posición se encuentra un determinado número. Proponga una
# solución utilizando división y conquista.

def buscar_numero(matriz, numero):
    return _buscar_numero(matriz, numero, 0, len(matriz), 0, len(matriz[0]))

def _buscar_numero(matriz, numero, inicio_x, fin_x, inicio_y, fin_y):
    if inicio_x == fin_x and inicio_y == fin_y:
        return (inicio_x, inicio_y)
    medio_x = (inicio_x+fin_x)//2
    medio_y = (inicio_y+fin_y)//2
    if matriz[medio_x][medio_y] == numero:
        return (medio_x, medio_y)
    if matriz[medio_x][medio_y] < numero:
        return _buscar_numero(matriz, numero, medio_x, fin_x, medio_y, fin_y)
    return _buscar_numero(matriz, numero, inicio_x, medio_x, inicio_y, medio_y)