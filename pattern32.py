"""
* * * * * * * * *
        * * * *
        * * *
        * *
        *
"""
# Take Input From User
n = int(input('Enter Your Number : '))
# print the first line * 9 times means
# n*2-1
print('* ' * (n * 2 - 1))
# Create a loop to print single space
# and decreasing order pattern
for i in range(n - 1, 0, -1):
    print('  ' * (n - 1) + '* ' * i)
