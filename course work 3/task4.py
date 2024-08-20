


def Difference(arr, m):
    # edge case handle
    if m == 0 or len(arr) == 0:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Number of packets
    n = len(arr)
    
    # If there are fewer packets than students
    if n < m:
        return -1  
    
    # Find the minimum difference
    y = float('inf')
    
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
           y = diff
    
    return y