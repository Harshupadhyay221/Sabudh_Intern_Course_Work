## Problem 1
## Read an integer N. For all non-negative integers i < N, print i^2. 

x = int(input('Please Enter Integer:'))
if x > 0:
    y = []  
    for i in range(x):
        y.append(i * i) 
    print(y)  
else:
    print('Please Enter Positive Integer')



## APPROACH : To read whether integer is postive or negative we put a condition. if our number is greater then zero
## then it is positive and if it is less then zero then it is negative.
## Then We initialize an empty list to store the squares
## Then we use for loop to append the square of the current , number to the list 
## Then we print the list of squares(y)

