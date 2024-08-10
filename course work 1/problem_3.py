## Problem Write a program to display only those numbers from a list that satisfy the following conditions
'''The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop'''

x = int(input('Enter the integer: '))
y = []
for i in range(1, x + 1):
    if i > 500:
        break
    if i > 150:
        continue
    if i % 5 == 0:
        y.append(i)

print(y)

## Approach 
# After taking an input from user we create an empty list as y[]
# We use for loop to iterate from 1 to the input number
# We check if the number is greater than 500, then break the loop
# We check if the number is greater than 150, then continue the loop
# We check if the number is divisible by 5, then append the number to the list y
