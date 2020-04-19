"""
        *
        * *
        * * *
        * * * *
* * * * * * * * *
"""
# Take Input From User
n = int(input('Enter Your Number : '))
# Create a loop to Print Spaces and
# Increasing * Pattern from 1 to n
for i in range(1, n):
    print('  ' * (n - 1) + '* ' * i)
# print the last line * 9 times means
# n*2-1
print('* ' * (n * 2 - 1))
