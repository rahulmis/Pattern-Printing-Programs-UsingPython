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
n = int(input("Enter number of lines : "))
for i in range(1, n + 1):
    print(' ' * (n - i) + '* ' * i)
for j in range(1, n):
    print(' ' * j + '* ' * (n - j))