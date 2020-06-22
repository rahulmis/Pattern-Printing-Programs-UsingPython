"""
        * *
      * * * *
    * * * * * *
  * * * * * * * *
* * * * * * * * * *
        * *
        * *
        * *
        * *
"""

n = int(input('Enter Your Number : '))
for i in range(1,n+1):
    print('  '*(n-i)+'* * '*i)
for i in range(1,n):
    print('  '*(n-1)+'* *')
