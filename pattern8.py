"""
*  *  *  *  *
*           *
*           *
*           *
*  *  *  *  *
"""
n = int(input("Enter Your Number : "))
print("*  "*n)
for i in range(n-2):
    print("*"+" "*((n-1)*3-1)+"*")
print("*  "*n)
