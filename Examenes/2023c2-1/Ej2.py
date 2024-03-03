# Dado un arreglo de n enteros, encontrar el subarreglo contiguo de máxima suma, utilizando División y Conquista.
# Indicar y justificar la complejidad del algoritmo.

# Lo resuelvo con el algoritmo de Kadane, pero en vez de recorrer el arreglo una vez, lo hago con divide y conquista
# donde en cada paso divido el arreglo en dos y me quedo con el maximo de la suma de los prefijos y sufijos de cada mitad
# y el maximo de la suma que cruza el medio.

def max_subarray(arr):
    return max_subarray_rec(arr, 0, len(arr) - 1)

def max_subarray_rec(arr, l, r): # O(nlogn)
    if l == r:
        return arr[l]
    m = (l + r) // 2
    max_izq = max_subarray_rec(arr, l, m)
    max_der = max_subarray_rec(arr, m + 1, r)
    max_cruz = max_subarray_cruz(arr, l, m, r)
    return max(max_izq, max_der, max_cruz)

def max_subarray_cruz(arr, l, m, r): # O(n)
    max_izq = float('-inf')
    suma = 0
    for i in range(m, l - 1, -1):
        suma += arr[i]
        max_izq = max(max_izq, suma)
    max_der = float('-inf')
    suma = 0
    for i in range(m + 1, r + 1):
        suma += arr[i]
        max_der = max(max_der, suma)
    return max_izq + max_der

# La complejidad del algoritmo es O(nlogn) ya que en cada paso divido el arreglo en dos y hago O(n) operaciones para
# encontrar la suma maxima que cruza el medio.