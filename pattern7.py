"""
    *
   ***
  *****
 *******
*********
"""
n = int(input("Enter your Number :"))
count = 1
for i in range(n,-1,-1):
    print(' '*i+"*"*count)
    count += 2
