"""
        *
      * *
    * * *
  * * * *
* * * * *
        *
        *
        *
        *
"""
# Take Input From User
n = int(input('Enter Your Number : '))
# Create a loop to Print Increasing * Pattern
# from 1 to n+1
for i in range(1, n + 1):
    print('  ' * (n - i) + '* ' * i)
# Create a loop to print single * pattern 
# the single STAR is n-1 times
for j in range(n - 1):
    print('  ' * (n - 1) + '*')
