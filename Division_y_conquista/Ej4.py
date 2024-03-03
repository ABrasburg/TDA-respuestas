# Dado un vector A de “n” números enteros (tanto positivos como negativos) queremos obtener el subvector cuya suma de elementos sea mayor a la suma de cualquier otro subvector en A.  
# Ejemplo: Array: [-2, -5, 6, -2, -3, 1, 5, -6]. Solución: [6, -2, -3, 1, 5]. Resolver el problema de subarreglo de suma máxima por división y conquista.

def maxCrossingSubarray(arr, l, m, h):
    left_sum = float('-inf')
    sm = 0
    max_left = m
    for i in range(m, l - 1, -1):
        sm += arr[i]
        if sm > left_sum:
            left_sum = sm
            max_left = i

    right_sum = float('-inf')
    sm = 0
    max_right = m
    for i in range(m + 1, h + 1):
        sm += arr[i]
        if sm > right_sum:
            right_sum = sm
            max_right = i

    return arr[max_left:max_right + 1]

def maxSubarray(arr, l, h):
    if l == h:
        return [arr[l]]

    m = (l + h) // 2

    left_subarray = maxSubarray(arr, l, m)
    right_subarray = maxSubarray(arr, m + 1, h)
    crossing_subarray = maxCrossingSubarray(arr, l, m, h)

    if sum(left_subarray) >= sum(right_subarray) and sum(left_subarray) >= sum(crossing_subarray):
        return left_subarray
    elif sum(right_subarray) >= sum(left_subarray) and sum(right_subarray) >= sum(crossing_subarray):
        return right_subarray
    else:
        return crossing_subarray
  
# Driver Code 
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
n = len(arr) 
  
max_sum = maxSubarray(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum) 