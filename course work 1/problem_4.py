#PROBLEM 4 
# Write a program to count the total number of digits in a number using a while loop

x = int(input('Enter integer: '))
count = 0

# Handle the case where the number is 0
if x == 0:
    count = 1
else:
    while x > 0:
        x = x // 10
        count += 1

print("Total number of digits:", count)

#Approach
#1. Take input from user
#2. Check if the number is 0, if yes then count = 1
#3. If not then count the number of digits in the number using while loop
#4. Here We use Bit Extraction Method for count the bit after extraction a bit we increase the count by 1
