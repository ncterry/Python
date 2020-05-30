"""
Given a 32-bit signed integer, reverse the digits.

Input 123       -->     Output 321
Input 120       -->     Output 21

We take the last number and set to tmp
We take the first number and set to last
We take tmp and set to first

We can't cycle through ints, and we cant alter strings.
We need to make a 2 step conversion from int -> string -> list
    Then we can alter the list, and then revert back to an int.
"""

class Solution():

    def reverse(self, number):
        snumber = str(number)                   # cant cycle through int, convert to string.
        lnumber = list(snumber)                 # string is immutable, change to list
        for x in range(0, len(snumber)):        # swap beginning/end through for loop with a temp-var
            tmp = snumber[len(lnumber) - x - 1]
            lnumber[len(lnumber) - x - 1] = snumber[x]
            lnumber[x] = tmp
        snumber = "".join(lnumber)              # list --> string
        number = int(snumber)                   # string --> int
        print(number)


try1 = Solution()
try1.reverse(123456789)