# Se realiza un torneo con n jugadores en el cual cada jugador juega con todos los otros n-1. El resultado del partido solo permite la victoria o la derrota.
# Se cuenta con los resultados almacenados en una matriz. Queremos ordenar los jugadores como P1, P2, …, Pn tal que P1 le gana a P2, P2 le gana a P3, …, Pn-1 le gana a Pn
# (La relación “le gana a” no es transitiva). Ejemplo: P1 le gana a P3, P2  le gana a P1 y P3 le gana a P2. Solución: [P1, P3, P2].
# Resolver por división y conquista con una complejidad no mayor a O(n log n).

def merge(left, right, results):
    i = j = 0
    sorted_players = []

    while i < len(left) and j < len(right):
        if results[left[i]][right[j]] == "W":
            sorted_players.append(left[i])
            i += 1
        else:
            sorted_players.append(right[j])
            j += 1

    sorted_players.extend(left[i:])
    sorted_players.extend(right[j:])

    return sorted_players

def sort_players(players, results):
    if len(players) <= 1:
        return players

    mid = len(players) // 2
    left = players[:mid]
    right = players[mid:]

    left_sorted = sort_players(left, results)
    right_sorted = sort_players(right, results)

    return merge(left_sorted, right_sorted, results)

# Ejemplo de uso
players = ["P1", "P2", "P3", "P4", "P5"]
results = {
    "P1": {"P1": "-", "P2": "W", "P3": "W", "P4": "L", "P5": "W"},
    "P2": {"P1": "L", "P2": "-", "P3": "L", "P4": "W", "P5": "W"},
    "P3": {"P1": "L", "P2": "W", "P3": "-", "P4": "W", "P5": "W"},
    "P4": {"P1": "W", "P2": "L", "P3": "L", "P4": "-", "P5": "L"},
    "P5": {"P1": "L", "P2": "L", "P3": "L", "P4": "W", "P5": "-"}
}

sorted_players = sort_players(players, results)
print("Jugadores ordenados:", sorted_players)