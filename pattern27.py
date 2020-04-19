"""
          *
          *
          *
          *
*         *         *
  *       *       *
    *     *     *
      *   *   *
          *
"""

# Take the input from the user
n = int(input('Enter Your Number : '))
#run the loop n-1 times because we see that
# the single * line is 4 times if n = 4
for i in range(n - 1): 
  # before the * wee see that there is 10
  # spaces so we take 2 space in print
  # and multiple it by n so n*2 = 10
    print('  ' * n + '*')
# print can count that the three * printing 
# sequence is run n-1 times if n = 5 then 4 
# so run loop 4 times 1 to n = 1,2,3,4
# 5 will be discarted in loops
for j in range(1, n): 
#first print spaces before first star which is 0,2,4,6,8
# j will run 1,2,3,4 if 1-1 then 0 and 2-1 then 1 so on 
# if we will mulitply it by 2 spaces it gives 0,2,4,6,8 spaces
# next count spaces after start which is 9,7,5,3 so print
# a space with * like '* ' then we need 8,6,4,2 space 
# print star and again repeat this count space after start
    print('  '*(j-1)+'* '+'  '*(n - j)+'*'+'  '*(n-j)+' *')
  # print the last start which is after 10 spaces 
print('  ' * n + '*')
