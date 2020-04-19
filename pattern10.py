"""
55555
 4444
  333
   22
    1
"""
n = int(input('Enter Number : '))
for i in range(n, 0, -1):
    print(" " * (n - i) + (str(i)) * i)
