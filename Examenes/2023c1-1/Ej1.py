# Se está formando una nueva comisión de actividades culturales de un pueblo. Cada habitante es miembro de 0 o más
# clubes, y de exactamente 1 partido político. Cada grupo de interés debe nombrar a un representante ante la nueva
# comisión de actividades culturales, con las siguientes restricciones: cada partido político no puede tener más de N/2
# simpatizantes en la comisión, cada persona puede representar a solo un club, cada club debe estar representado por
# un miembro. Implementar un algoritmo que dada la información de los habitantes (a qué clubes son miembros, a
# qué partido pertenecen), nos dé una lista de representantes válidos. Indicar y justificar la complejidad del algoritmo
# implementado.

# La idea es recorrer a los habitantes, y para cada habitante, ver si ya hay un representante de su partido político.
# Si no lo hay, lo agregamos a la lista de representantes. Si ya lo hay, vemos si ya hay un representante de su club.
# Si no lo hay, lo agregamos a la lista de representantes. Si ya lo hay, no lo agregamos.
# O(n^2) en el peor caso, ya que para cada habitante, recorremos la lista de representantes para ver si ya hay uno de su
# partido político y de su club.
def representantes(habitantes, N):
    representantes = []
    partidos_representados = []
    clubes_representados = []
    for habitante in habitantes:
        partido = habitante[1]
        clubes = habitante[0]
        if partidos_representados.count(partido) < N/2:
            if not partido in partidos_representados:
                representantes.append(habitante)
                partidos_representados.append(partido)
            for club in clubes:
                if not club in clubes_representados:
                    for c in clubes:
                        if c not in clubes_representados:
                            clubes_representados.append(c)
                    representantes.append(habitante)
                    break
    # Valido que no haya más de N/2 representantes por partido
    partidos = [r[1] for r in representantes]
    for partido in partidos:
        if partidos.count(partido) > N/2:
            # Agrego uno de otro partido
            for habitante in habitantes:
                if habitante[1] != partido:
                    representantes.append(habitante)
                    break
                    
    return representantes