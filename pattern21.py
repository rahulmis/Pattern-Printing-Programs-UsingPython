"""
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
"""
n = int(input("Enter your number : "))
for i in range(n, 0, -1):
    print('* ' * i + '  ' * ((n - i) * 2) + '* ' * i)
