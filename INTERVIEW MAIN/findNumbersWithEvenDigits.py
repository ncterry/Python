"""
Given an array nums of integers, return how many of them contain an even number of digits.
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
    12 contains 2 digits (even number of digits).
    345 contains 3 digits (odd number of digits).
    2 contains 1 digit (odd number of digits).
    6 contains 1 digit (odd number of digits).
    7896 contains 4 digits (even number of digits).
"""

print("")
def findNumberWithEvenDigits(numlist):
    for i in range(len(numlist)):
        if len(str(numlist[i])) % 2 == 0:
            print(f'{numlist[i]} contains {len(str(numlist[i]))} digits (even number of digits).')

        else:
            print(f'{numlist[i]} contains {len(str(numlist[i]))} digits (odd number of digits).')



# --------------------------------------


findNumberWithEvenDigits([12,345,2,6,7896])

