# Esta peculiar empresa se dedica a cubrir patios cuadrados de n*n metros (“n” es un número entero potencia de 2 y mayor
# o igual a 2). Cuenta con baldosas especiales que tienen forma en L (como se muestra en celeste en la imágen).
# Las baldosas no se pueden cortar. Todo patio cuenta con un único sumidero de agua de lluvia. Ocupa 1x1 metro y su
# ubicación depende del patio (Se muestra en la figura de ejemplo como un cuadrado negro).
# Nos piden que, dado un patio con un valor “n” y una ubicación del sumidero en una posición x,y desde la punta superior
# izquierda, determinemos cómo ubicar las baldosas. Presentar un algoritmo que lo resuelva utilizando división y conquista.

def baldosas(n, posicion_sum):
    # Me creo una matriz vacia
    matriz = []
    for i in range(n):
        linea = [' '] * n
        matriz.append(linea)
    matriz[posicion_sum[0]][posicion_sum[1]] = 's'
    # Me fijo en que cuadrante esta el sumidero
    cuadrante = 0
    if posicion_sum[0] > 1:
        if posicion_sum[1] > 1:
            cuadrante = 3
        else:
            cuadrante = 1
    else:
        if posicion_sum[1] > 1:
            cuadrante = 2
        else:
            cuadrante = 0
    return _baldosas(0, n, 0, n, matriz, posicion_sum, cuadrante, cuadrante)

def _baldosas(inicio_x, fin_x, inicio_y, fin_y, matriz, posicion_sum, cuadrante_sum, cuadrante_actual):
    if inicio_x-fin_x == 2 and inicio_y-fin_y == 2:
        # Me fijo cual de los 4 esta cubierto y pongo las baldosas correspondientes
        if matriz[inicio_x][inicio_y] != ' ':
            if matriz[inicio_x][inicio_y+1] != ' ':
                if matriz[inicio_x+1][inicio_y] != ' ':
                    matriz[inicio_x+1][inicio_y+1] = 'L'
                else:
                    matriz[inicio_x+1][inicio_y] = 'L'
            else:
                matriz[inicio_x][inicio_y+1] = 'L'
        else:
            matriz[inicio_x][inicio_y] = 'L'
        return 
    # El sumidero esta en el cuadrante cuadrante
    medio_x = (inicio_x+fin_x)//2
    medio_y = (inicio_y+fin_y)//2
    if cuadrante_actual == 0:
        matriz[medio_x+1][medio_y+1] = 'C'
        matriz[medio_x][medio_y+1] = 'C'
        matriz[medio_x+1][medio_y] = 'C'
    else if cuadrante_actual == 1:
        matriz[medio_x+1][medio_y+1] = 'C'
        matriz[medio_x][medio_y] = 'C'
        matriz[medio_x][medio_y+1] = 'C'
    _baldosas(inicio_x, medio_x, inicio_y, medio_y, matriz, posicion_sum, cuadrante)
    _baldosas(inicio_x, medio_x, medio_y, fin_y, matriz, posicion_sum, 1)
    _baldosas(medio_x, fin_x, inicio_y, medio_y, matriz, posicion_sum, 2)
    _baldosas(medio_x, fin_x, medio_y, fin_y, matriz, posicion_sum, 3)
    return matriz

print(baldosas(4, (2,2)))