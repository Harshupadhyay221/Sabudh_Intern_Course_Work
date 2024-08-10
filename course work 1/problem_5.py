#PROBLEM 5
## Write a program to calculate the sum of series up to n term. For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
n = int(input('Enter Integer :'))
def sum_of_series(n):
    series_sum = 0
    term = 0
    
    for i in range(1, n+1):
        term = term * 10 + 2
        series_sum += term
    
    return series_sum

# Test Case 1
result = sum_of_series(n)
print(f"Input: {n}")
print(f"Output: {result}")

## Approach
# 1. Initialize the series_sum to 0 and term to 0
# 2. Iterate from 1 to n+1
# 3. For each iteration, multiply term by 10 and add 2 to it
# 4. Add the term to series_sum
