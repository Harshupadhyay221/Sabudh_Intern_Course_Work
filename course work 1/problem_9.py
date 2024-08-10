
## Problem 9
#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.


n = int(input('Enter integrer : '))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

result = factorial(n)
print("Factorial is:", result)

# Approach
# A factorial number is a concept in mathematics 
# defined as the product of all positive integers up to a given number. 

# 1. If n is 0, then factorial is 1
# 2. If n is not 0, then factorial is n * factorial(n-1


    
