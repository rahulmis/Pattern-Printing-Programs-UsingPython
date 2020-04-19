"""
        *
          *
            *
              *
* * * * * * * * *
              *
            *
          *
        *
"""
# Take Input From User
n = int(input('Enter Your number : '))
# count spaces before * is 8 then 10 then 12.. 
cc = (n - 1) * 2 # this will give 8 for spaces
for i in range(1, n): # run a loop 4 times 
  #this will print first 8 spaces and *
    print(' ' * (cc) + '*')
    # increase the spaces count so it 
    #will print 10 spaces next iteration
    cc += 2
# Creating The Pattern Middle Line
print('* ' * ((n * 2) - 1))
# Code For Create Bottom Pattern After Horizontal line
cc1 = n * 4 - 6 #count spaces which is 14 then * 
for i in range(n - 1, 0, -1):
  #cc1 = 14 when n = 5 so will print 14 space then *
    print(' ' * (cc1) + '*')
    #reduce the cc1 -2 for the next line
    cc1 -= 2
