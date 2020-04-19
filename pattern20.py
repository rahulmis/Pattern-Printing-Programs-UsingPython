"""
*                 *
* *             * *
* * *         * * *
* * * *     * * * *
* * * * * * * * * *
"""
n = int(input('Enter Your number : '))
for i in range(1, n + 1):
    print('* ' * i + '  ' * ((n - i) * 2) + '* ' * i)
