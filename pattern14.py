"""
        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *
"""
n = int(input('Enter Number : '))
for i in range(1, n + 1):
    print('  ' * (n - i) + '* ' * i)
for j in range(1, n):
    print('  ' * j + '* ' * (n - j))
