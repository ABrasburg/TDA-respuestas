# Problema de la mochila con igual peso y valor con backtracking

def _max_cant_personas_mesa(P, W, sol_parcial): # Aprox
    if len(P) == 0:
        return sum(sol_parcial)
    if P[0] <= W:
        sol_parcial.append(P[0])
        con = _max_cant_personas_mesa(P[1:], W-P[0], sol_parcial)
        sol_parcial.pop()
        sin = _max_cant_personas_mesa(P[1:], W, sol_parcial)
        return max(con, sin)
    return _max_cant_personas_mesa(P[1:], W, sol_parcial)

def max_cant_personas_mesa(P, W):
    sol_parcial = []
    return _max_cant_personas_mesa(P, W, sol_parcial)

P = [2, 3, 4, 5]
W = 10
print(max_cant_personas_mesa(P, W)) # 9