# Para determinar si un número es primo existen varios algoritmos propuestos. Entre ellos el test de Fermat. Este es un
# algoritmo randomizado que opera de la siguiente manera: Dado un número entero “n”, seleccionar de forma aleatoria un
# número entero “a” coprimo a n. Calcular an-1 módulo n. Si el resultado es diferente a 1, entonces el número “n” es
# compuesto. La parte central de esta operatoria es la potenciación. Podríamos algorítmicamente realizarla de la
# siguiente manera:

# pot = 1
# Desde i=1 a n-1
#     pot = pot * a
# En este caso se realizan o(n) multiplicaciones. Proponga un método usando división y conquista que resuelva la potenciación con menor complejidad temporal. 

# Implemente la función potenciacion(a, n) que recibe dos números enteros y devuelve a elevado a la n.

def potenciacion(a, n): # O(log n)
    if n == 0:
        return 1
    if n % 2 == 0:
        return potenciacion(a, n//2) * potenciacion(a, n//2)
    else:
        return a * potenciacion(a, n//2) * potenciacion(a, n//2)
    
print(potenciacion(2, 4)) # 16

def Fermat(n, k): # O(k * log n)
    import random
    for i in range(k):
        a = random.randint(2, n-1)
        if potenciacion(a, n-1) % n != 1:
            return False
    return True

print(Fermat(6, 3)) # True