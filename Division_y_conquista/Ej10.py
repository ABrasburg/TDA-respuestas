# Todos los años la asociación de un importante deporte individual profesional realiza una preclasificación de los n
# jugadores que terminaron en las mejores posiciones del ranking para un evento exclusivo. En la tarjeta de invitación
# adjuntan el número de posición en la que está actualmente y a cuantos rivales invitados superó en el ranking comparado
# el año pasado. Contamos con un listado que tiene el nombre del jugador y la posición del ranking del año pasado
# ordenado por el ranking actual. Ejemplo: LISTA: A,3 | B,4 | C,2 | D,8 | E,6 | F,5. Se puede ver que el jugador “A”
# superó al jugador “C”. El jugador “B” superó al jugador “C”. El jugador “C” no superó a ninguno de los invitados.
# Etc. Proponer una solución utilizando la metodología de división y conquista.

def buscar_jugador(lista, jugador):
    return _buscar_jugador(lista, jugador, 0, len(lista))

def _buscar_jugador(lista, jugador, inicio, fin):
    if inicio == fin:
        return inicio
    medio = (inicio+fin)//2
    if lista[medio][0] == jugador:
        return medio
    if lista[medio][0] < jugador:
        return _buscar_jugador(lista, jugador, medio, fin)
    return _buscar_jugador(lista, jugador, inicio, medio)