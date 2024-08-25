#Given an array of 2n elements in the following format { a1, a2, a3, a4, ….., an, b1, b2, b3, b4, …., bn }. The task is to shuffle the array to {a1, b1, a2, b2, a3, b3, ……, an, bn } without using extra space. 
# Swap Alternate elements of an array

def shuffle(arr, n):
    for i in range(1, n):
        j = i
        while j < n:
            # Swap the elements
            arr[j], arr[n + j] = arr[n + j], arr[j]
            j += 1
    return arr

## Example usage
arr1 = [1, 2, 9, 15]
n1 = len(arr1) // 2
print(shuffle(arr1, n1))  # Output: [1, 9, 2, 15]

# WE ALSO USE TWO POINTER APPROACH FOR THIS 