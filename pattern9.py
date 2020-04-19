"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
n = int(input("Enter Your Number : "))
for i in range(n,0,-1):
    print((str(i)+" ")*i)