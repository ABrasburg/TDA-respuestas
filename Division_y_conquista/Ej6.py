# A raíz de una nueva regulación industrial un fabricante debe rotular cada lote que produce según un valor numérico que
# lo caracteriza. Cada lote está conformado por “n” piezas. A cada una de ellas se le realiza una medición de volumen. 
# La regulación considera que el lote es válido si más de la mitad de las piezas tienen el mismo volumen. En ese caso el
# rótulo deberá ser ese valor. De lo contrario el lote se descarta. Actualmente cuenta con el proceso “A” que consiste en 
# para cada pieza del lote contar cuántas de las restantes tienen el mismo volumen. Si alguna de las piezas corresponde al
# “elemento mayoritario”, lo rotula. De lo contrario lo rechaza. Un consultor informático impulsa una solución (proceso “B”)
# que considera la más eficiente: ordenar las piezas por volumen y con ello luego reducir el tiempo de búsqueda del 
# elemento mayoritario. Nos contratan para construir una solución mejor (proceso “C”). Se pide: 
# a) Exprese mediante pseudocódigo el proceso “A”.
# b) Explique si la sugerencia del consultor (proceso “B”) realmente puede mejorar el proceso. En caso afirmativo, 
# arme el pseudocódigo que lo ilustre.
# c) Proponga el proceso “C” como un algoritmo superador mediante división y conquista. 
# Explíquelo detalladamente y brinde pseudocódigo.

# a) Proceso A
# def majority_element(A):
#     para cada elemento en A:
#         contador = 0
#         para cada elemento en A:
#             si elemento == elemento:
#                 contador += 1
#         si contador > len(A) / 2:
#             devolver elemento
#     devolver None
# Este proceso es O(n^2) ya que recorre la lista A dos veces.

# b) Proceso B
# Ordenar una lista de n elementos es O(n log n) usando mergesort o quicksort. Luego, buscar el elemento mayoritario es O(n).
# Por lo tanto, el proceso B es O(n log n) + O(n) = O(n log n).
# def majority_element(A):
#     A.sort()
#     contador = 0
#     for i in range(len(A)):
#         if A[i] == A[i + 1]:
#             contador += 1
#         else:
#             contador = 0
#         if contador > len(A) / 2:
#             return A[i]
#     return None

# c) Proceso C
# La idea es usar un algoritmo de división y conquista para encontrar el elemento mayoritario en O(n log n).
def majority_element(A):
    if len(A) == 1:
        return A[0]
    
    mid = len(A) // 2
    left = majority_element(A[:mid])
    right = majority_element(A[mid:])

    if left == right:
        return left

    left_count = A.count(left) # O(n)
    right_count = A.count(right)

    if left_count > len(A) / 2:
        return left
    elif right_count > len(A) / 2:
        return right
    else:
        return None
