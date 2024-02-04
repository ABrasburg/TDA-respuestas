# Dado un vector A de “n” números enteros (tanto positivos como negativos) queremos obtener el subvector cuya suma de elementos sea mayor a la suma de cualquier otro subvector en A.  
# Ejemplo: Array: [-2, -5, 6, -2, -3, 1, 5, -6]. Solución: [6, -2, -3, 1, 5]. Resolver el problema de subarreglo de suma máxima por división y conquista.

def maxCrossingSum(arr, l, m, h): 
  
    # Include elements on left of mid. 
    sm = 0
    left_sum = -10000
  
    for i in range(m, l-1, -1): 
        sm = sm + arr[i] 
  
        if (sm > left_sum): 
            left_sum = sm 
  
    # Include elements on right of mid 
    sm = 0
    right_sum = -1000
    for i in range(m, h + 1): 
        sm = sm + arr[i] 
  
        if (sm > right_sum): 
            right_sum = sm 
  
    # Return sum of elements on left and right of mid 
    # returning only left_sum + right_sum will fail for [-2, 1] 
    return max(left_sum + right_sum - arr[m], left_sum, right_sum) 
  
  
# Returns sum of maximum sum subarray in aa[l..h] 
def maxSubArraySum(arr, l, h): 
    #Invalid Range: low is greater than high 
    if (l > h): 
        return -10000
    # Base Case: Only one element 
    if (l == h): 
        return arr[l] 
  
    # Find middle point 
    m = (l + h) // 2
  
    # Return maximum of following three possible cases 
    # a) Maximum subarray sum in left half 
    # b) Maximum subarray sum in right half 
    # c) Maximum subarray sum such that the 
    #     subarray crosses the midpoint 
    return max(maxSubArraySum(arr, l, m-1), 
               maxSubArraySum(arr, m+1, h), 
               maxCrossingSum(arr, l, m, h)) 
  
  
# Driver Code 
arr = [-2, -5, 6, -2, -3, 1, 5, -6]
n = len(arr) 
  
max_sum = maxSubArraySum(arr, 0, n-1) 
print("Maximum contiguous sum is ", max_sum) 