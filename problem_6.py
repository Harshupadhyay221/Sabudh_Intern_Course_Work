# Problem 6
#Write a program to Reverse below given numbers without slicing

x = int(input('Enter Integer'))
revnum = 0
while x > 0:
    # for reverse a number we use bit extraction 
    rem = x % 10
    revnum = revnum * 10 + rem
    x = x // 10

print('Reverse Number is', revnum)
 
# Approach
#1. Take input from user 
#2. Initialize variable revnum = 0
#3. While loop to iterate till x > 0
#4. Take remainder of x and store in rem variable
#5. Multiply revnum by 10 and add rem to revnum
#6. Divide x by 10 and store in x variable
