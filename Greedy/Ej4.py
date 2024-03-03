# Para la realización del próximo congreso de “charlas motivacionales para el joven de hoy” se contrató un hotel que
# cuenta con m salas de exposición. Existirán “n” oradores. Cada uno solicitó un tiempo de exposición definido por un
# horario de ingreso y una duración. Los organizadores quieren asignar las salas con un intervalo entre charla y charla
# de 15 minutos y desean utilizar la menor cantidad de salas posibles. Presentar un algoritmo greedy que resuelve el
# problema indicando la cantidad de salas a utilizar y la asignación de las charlas. En caso de sobrepasar el máximo de
# salas disponibles informar. Analice complejidad y optimalidad 

# Ordeno por horario de fin y siempre asigno la sala con el horario de fin más temprano. Si no hay salas disponibles, se
# descarta la charla. Complejidad O(n log n) por el ordenamiento.

def charlas(oradores, m):
    finales = []
    for o in oradores:
        finales.append((o[0] + o[1], o))
    finales.sort(key=lambda x: x[0])
    salas = []
    for i in range(m):
        salas.append([])
    for s in salas:
        for f in finales:
            if len(s) == 0 or s[-1][0] <= f[1][0]:
                s.append(f[1])
                finales.remove(f)
    if len(finales) > 0:
        return "No hay suficientes salas"
    return salas

oradores = [(0, 30), (15, 30), (30, 30), (45, 30)]
m = 3
print(charlas(oradores, m))