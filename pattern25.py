"""
        *
      *
    *
  *
* * * * * * * * *
  *
    *
      *
        *
"""
# Take Input From User
n = int(input('Enter Your Value : '))
# Create Pattern Before The Horizontal Line
for i in range(1, n):
    print(' ' * ((n - i) * 2) + '*')
# Creating The Pattern Middle Line
print('* ' * (n * 2 - 1))
# Code For Create Bottom Pattern After Horizontal line
for i in range(n - 1, 0, -1):
    print(' ' * ((n - i) * 2) + '*')
