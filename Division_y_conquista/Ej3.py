# Se cuenta con un vector de “n” posiciones en el que se encuentran algunos de los primeros ”m” números naturales ordenados en forma creciente (m >= n). 
# En el vector no hay números repetidos. Se desea obtener el menor número no incluido. Ejemplo: [1, 2, 3, 4, 5, 8, 9, 11, 12, 13, 14, 20, 22]. 
# Solución: 6. Proponer un algoritmo de tipo división y conquista que resuelva el problema en tiempo inferior a lineal. Expresar su relación de recurrencia y calcular su complejidad temporal.

def min_not_included(numbers, start, end): # No uso el numero 0
    # Caso base
    if start == end:
        return start+1
    
    medio = (start + end) // 2
    if numbers[medio] > medio+1:
        return min_not_included(numbers, start, medio)
    elif numbers[medio] >= medio+1:
        return min_not_included(numbers, medio+1, end)
    
numbers = [1, 2, 3, 4, 5,6,7, 8, 9,10, 11, 12, 13, 14, 20, 22]
print(min_not_included(numbers, 0, len(numbers)-1))  # 6

# La relación de recurrencia es T(n) = T(n/2) + O(1), que tiene complejidad O(log n).