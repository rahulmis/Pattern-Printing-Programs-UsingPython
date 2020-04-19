"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
n = int(input('Enter Your Number :'))

for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
