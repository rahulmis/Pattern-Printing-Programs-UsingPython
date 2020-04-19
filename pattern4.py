"""
A
B C
D E F
G H I J
K L M N O
"""
# for number to character >>> chr(67)
#for character to number >>> ord("a")
n = int(input("Enter number of lines :"))
cc = 65
for i in range(1,n+1):
    for j in range(i):
        print(chr(cc),end=' ')
        cc += 1
    print()