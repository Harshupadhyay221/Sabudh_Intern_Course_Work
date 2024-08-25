#Given two sorted arrays, a[] and b[], the task is to find the median of these sorted arrays, where N is the number of elements in the first array, and M is the number of elements in the second array.

def median(a, b):
    # Merge the two sorted arrays
    merged = sorted(a + b)
    
    # Calculate the length of the merged array
    n = len(merged)
    
    # Find the median
    if n % 2 == 1:  # Odd length
        return merged[n // 2]
    else:  # Even length
        return (merged[(n // 2) - 1] + merged[n // 2]) / 2
    
