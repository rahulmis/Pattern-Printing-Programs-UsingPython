"""
*
* *
* * *
* * * *
* * * * *
*
*
*
*
"""
#take input from user
n = int(input('Enter Your Number : '))
# we can divide the pattern into two parts 
# the first one is 1 to 5th line where the star
# prints in increasing order and second is only single 
# star print lines
# take a loop to print first part increasing order stars 
for i in range(1, n + 1):
    print('* ' * i)
# take a loop to print n -1 times single star
for j in range(n - 1):
    print('*')
