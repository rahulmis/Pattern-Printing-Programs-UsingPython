"""
        * *
        * *
        * *
        * *

* * * * * * * * * *
  * * * * * * * *
    * * * * * *
      * * * *
        * *
"""
n = int(input('Enter Your Number : '))
for i in range(1, n):
    print('  ' * (n - 1) + '* *')
for i in range(n,0,-1):
    print('  '*(n-i)+'* * '*i)