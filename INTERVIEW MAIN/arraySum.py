"""
Given an array of integers, fin the sum of its elements.
EX: [1, 2, 3] -> Sum = 6
EX: [1, 2, 3, 4, 10, 11] == 31
"""

class Solution(object):

    def arraySum(self, arraysent, sum1):
        for n in range(len(arraysent)):
            sum1 = sum1 + arraysent[n]
        return sum1

array1 = [1, 2, 3]
array2 = [1, 2, 3, 4, 10, 11]

check1 = Solution()
print(f'Sum of Array: {array1} = {check1.arraySum(array1, 0)}')
print(f'Sum of Array: {array2} = {check1.arraySum(array2, 0)}')
