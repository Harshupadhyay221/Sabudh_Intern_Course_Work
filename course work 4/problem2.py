# Given an integer array, find a triplet having the maximum product.

def max_product(arr):
    # Sort the array
    arr.sort()

    # Calculate the product of the three largest numbers
    product1 = arr[-1] * arr[-2] * arr[-3]

    # Calculate the product of the two smallest numbers and the largest number
    product2 = arr[0] * arr[1] * arr[-1]

    # Return the maximum of the two products
    maxy = max(product1, product2)

    # Determine which triplet gave the max product
    if maxy == product1:
        triplet = (arr[-3], arr[-2], arr[-1])
    else:
        triplet = (arr[0], arr[1], arr[-1])

    return triplet, maxy