"""
          *
      *   *   *
    *     *     *
  *       *       *
*         *         *

          *
          *
          *
          *
"""
# Take input from the user
n = int(input('Enter Your Number :'))
# print the single top star after n*2 = 10 spaces
print('  ' * n + '*')
# run a loop in which three stars ate prints
# wee see that the three stars print lines are n-1 means 
# 4 times so run a loop n-1 means 4 to 1 0 will be discarted
# and -1 is step sie it will reduce -1 in every iteration of 
# loop means first loop 4-1 tehn second 3-1 and so on
for i in range(n - 1, 0, -1):
# you can see this sequence is my previous post this is same 
    print('  '*(i-1)+'* '+'  '*(n-i)+'*'+'  '*(n-i)+' *')
# single star are of n-1 = 4 times so take n-1 times loop
for j in range(n - 1):
  # before the * we see that there is 10
  # spaces so we take 2 space in print
  # and multiple it by n so n*2 = 10
    print('  ' * n + '*')
