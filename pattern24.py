"""
* * * * * * * * *
  *           *
    *       *
      *   *
        *
"""
n = int(input('Enter Your number : '))
tt = n * 2 - 1
print('* ' * (tt))
tt = (tt * 2) - 7
for i in range(1, n - 1):
    print('  ' * i + '*' + ' ' * (tt) + '*')
    tt -= 4
print('  ' * (n - 1) + '*')
