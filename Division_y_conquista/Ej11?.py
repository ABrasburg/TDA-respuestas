# Una agencia gubernamental tiene un conjunto de "n" agentes dispersos por el país. Para una misión urgente requiere
# utilizar dos de ellos. Cada agente tiene una ubicación (x,y). Se dispone de un helicóptero para buscarlos.
# Generar una solución por división y conquista que indique cuáles son los 2 agentes más cercanos, cuál es su
# distancia y dónde debería ir el helicóptero a buscarlo.

import math

def distancia(p1, p2):
    """Calcula la distancia euclidiana entre dos puntos."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def encontrar_minima_distancia(agentes):
    """Función principal para encontrar los dos agentes más cercanos."""
    # Ordenar los agentes por coordenada x
    agentes_ordenados = sorted(agentes, key=lambda x: x[0])
    return encontrar_minima_distancia_recursiva(agentes_ordenados)

def encontrar_minima_distancia_recursiva(agentes):
    """Función recursiva para encontrar los dos agentes más cercanos."""
    n = len(agentes)
    
    # Caso base: si hay pocos agentes, usar fuerza bruta para encontrar la distancia mínima
    if n <= 3:
        return fuerza_bruta(agentes)

    # Dividir los agentes en dos mitades
    medio = n // 2
    punto_medio = agentes[medio][0]

    izquierda = agentes[:medio]
    derecha = agentes[medio:]

    # Encontrar la distancia mínima en cada mitad
    distancia_izquierda, agentes_izquierda = encontrar_minima_distancia_recursiva(izquierda)
    distancia_derecha, agentes_derecha = encontrar_minima_distancia_recursiva(derecha)

    # Tomar la distancia mínima entre las dos mitades
    minima_distancia_entre_mitades = min(distancia_izquierda, distancia_derecha)

    # Encontrar los agentes dentro de la franja central
    franja_central = []
    for agente in agentes:
        if abs(agente[0] - punto_medio) < minima_distancia_entre_mitades:
            franja_central.append(agente)

    # Calcular la distancia mínima dentro de la franja central
    franja_central_ordenada = sorted(franja_central, key=lambda x: x[1])
    minima_distancia_franja_central = float('inf')
    agentes_minima_distancia = None
    for i in range(len(franja_central_ordenada)):
        for j in range(i+1, len(franja_central_ordenada)):
            dist = distancia(franja_central_ordenada[i], franja_central_ordenada[j])
            if dist < minima_distancia_franja_central:
                minima_distancia_franja_central = dist
                agentes_minima_distancia = (franja_central_ordenada[i], franja_central_ordenada[j])

    # Devolver la distancia mínima y las posiciones de los dos agentes más cercanos
    if minima_distancia_franja_central < minima_distancia_entre_mitades:
        return minima_distancia_franja_central, agentes_minima_distancia
    else:
        if distancia_izquierda < distancia_derecha:
            return distancia_izquierda, agentes_izquierda
        else:
            return distancia_derecha, agentes_derecha

def fuerza_bruta(agentes):
    """Algoritmo de fuerza bruta para encontrar la distancia mínima entre agentes."""
    minima_distancia = float('inf')
    agentes_minima_distancia = None
    for i in range(len(agentes)):
        for j in range(i+1, len(agentes)):
            dist = distancia(agentes[i], agentes[j])
            if dist < minima_distancia:
                minima_distancia = dist
                agentes_minima_distancia = (agentes[i], agentes[j])
    return minima_distancia, agentes_minima_distancia

# Ejemplo de uso
agentes = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
minima_distancia, agentes_minima_distancia = encontrar_minima_distancia(agentes)
print("La distancia mínima entre dos agentes es:", minima_distancia)
print("Los agentes más cercanos están en las posiciones:", agentes_minima_distancia)
