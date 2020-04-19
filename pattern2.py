"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
n = int(input('Enter number for Pattern :'))
# for i in range(1,n+1):
#     print((str(i)+" ")*i)
###############################using while loop
cc = 1
while cc <= n:
    print((str(cc) + " ") * cc)
    cc += 1
