"""
     *
    * *
   *   *
  *     *
 *       *
  *     *
   *   *
    * *
     *
"""
n = int(input("enter your number : "))
print(' ' * n + '*')
for i in range(1, n - 1):
    print(' ' * (n - i) + '*' + ' ' * (i + i - 1) + '*')
for j in range(1, n):
    print(' ' * j + '*' + ' ' * (((n - j) * 2) - 1) + '*')
print(' ' * n + '*')
