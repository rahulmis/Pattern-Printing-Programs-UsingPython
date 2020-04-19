"""
    *   # 4 space then 1 *
   **   # 3 space then 2 *
  ***   # 2 space then 3 *
 ****   # 1 space then 4 *
*****   # 0 space then 5 *
"""

n = int(input('Enter your number :'))
for i in range(1,n+1):
    print(' '*(n-i)+"*"*i)


