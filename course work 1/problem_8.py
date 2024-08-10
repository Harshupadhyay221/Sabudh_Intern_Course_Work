# Problem 8
# Write a Python program to find the median of three values.


a = float(input('Enter the first value: '))
b = float(input('Enter the second value: '))
c = float(input('Enter the third value: '))

#Check if a is the Median:
if (a >= b and a <= c) or (a <= b and a >= c):
    median = a
#Check if b is the Median:  
elif (b >= a and b <= c) or (b <= a and b >= c):
    median = b
#Check if c is the Median:
else:
    median = c


print("Median:", median)

# Approach
# Median :TThe median of three numbers is the value that is neither the maximum nor the minimum; 
# it’s the middle value when sorted.

# 1. Take input to the users 
# 2. Checking for both a,b,c