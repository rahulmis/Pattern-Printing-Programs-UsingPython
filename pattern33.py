"""
        *
        * *
        * * *
        * * * *
* * * * * * * * *
* * * * * * * * *
        * * * *
        * * *
        * *
        *
"""
n = 5
for i in range(1,n):
    print('  '*(n-1)+'* '*i)
print('* '*(n*2-1))
print('* '*(n*2-1))
for i in range(n-1,0,-1):
    print('  '*(n-1)+'* '*i)
