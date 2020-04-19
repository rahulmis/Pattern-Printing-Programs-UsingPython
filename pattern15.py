"""
* * * * *
 * * * *
  * * *
   * *
    *
    *
   * *
  * * *
 * * * *
* * * * *
"""
n = int(input("Enter your number : "))
for i in range(n, 0, -1):
    print(' ' * (n - i) + '* ' * i)
for j in range(1, n + 1):
    print(' ' * (n - j) + '* ' * j)
