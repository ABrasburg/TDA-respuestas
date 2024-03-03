# Un bodegón tiene una única mesa larga con W lugares. Hay una persona en la puerta que anota los grupos que quieren
# sentarse a comer, y la cantidad de integrantes que conforma a cada uno. Para simplificar su trabajo, se los anota en
# un vector P donde P[i] contiene la cantidad de personas que integran el grupo i, siendo en total n grupos. Como se
# trata de un restaurante familiar, las personas sólo se sientan en la mesa si todos los integrantes de su grupo pueden
# sentarse. Implementar un algoritmo que, mediante programación dinámica, obtenga el conjunto de grupos que ocupan
# la mayor cantidad de espacios en la mesa (o en otras palabras, que dejan la menor cantidad de espacios vacíos). Indicar
# y justificar la complejidad del algoritmo.

# Lo resuelvo como el problema de la mochila, donde la capacidad de la mochila es W y los objetos son los grupos
# donde el peso es la cantidad de personas y el valor es la cantidad de personas
# O(n*W) en tiempo y O(n*W) en espacio

def max_cant_personas_mesa(P, W):
    matriz = crear_matriz(len(P), W)
    for obj in range(len(P)):
        for tam in range(W):
            if P[obj] > tam:
                continue
            if P[obj] + matriz[obj-1][tam-P[obj]] > matriz[obj-1][tam]:
                matriz[obj][tam] = P[obj] + matriz[obj-1][tam-P[obj]]
            else:
                matriz[obj][tam] = matriz[obj-1][tam]
    return matriz[-1][-1]

def crear_matriz(n, m):
    return [[0] * m for _ in range(n)]

P = [2, 3, 4, 5]
W = 10
print(max_cant_personas_mesa(P, W)) # 9