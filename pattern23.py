"""
        *
      *   *
    *       *
  *           *
* * * * * * * * *
"""
n = int(input('Enter value: '))
print('  '*(n-1)+'*')
cc = 1
for i in range(n-2,0,-1):
    print('  '*i+'* '+' '*(cc)+ ' *')
    cc += 4
print('* '*(n*2-1))