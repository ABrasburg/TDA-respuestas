# Implementar un algoritmo que, por división y conquista, dado un arreglo de n números enteros devuelva true o false
# según si existe algún elemento que aparezca más de dos tercios de las veces. El algoritmo debe ser O(n). Justificar la
# complejidad del algoritmo implementado.

def aparece_mas_de_dos_tercios(arr): # O(nlogn)
    return aparece_mas_de_dos_tercios_rec(arr, 0, len(arr) - 1)

def aparece_mas_de_dos_tercios_rec(arr, l, r): 
    if l == r:
        return False
    m = (l + r) // 2
    if arr.count(arr[m]) > len(arr) / 3:
        return True
    return aparece_mas_de_dos_tercios_rec(arr, l, m) or aparece_mas_de_dos_tercios_rec(arr, m + 1, r)

print(aparece_mas_de_dos_tercios([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # False
print(aparece_mas_de_dos_tercios([1, 2,1,2,1,1,2,1])) # True
