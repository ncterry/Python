"""
Given an array of integers and an integer  k
You need to find the total number of continues subarrays whose sum = k

EX. nums = [1,1,1], k=2
    Output = 2

Array length up to 20000
Numbers in array range from:   -1000 : 1000
k range from:   -1000000 : 1000000

"""

from random import randint

class Solution():

    def randomArray(self):
        subarray = []
        for i in range(0, 1000):
            subarray.append(randint(0, 1000))
        return subarray

    def subarraySum(self, thearray, k):
        for i in range(len(thearray)):
            count = 0
            total = 0
            for x in range(i, len(thearray)):
                total = total + thearray[x]
                count += 1
                if total == k:
                    print(f'Success!!!\n\tk = {k}\ttotal = {total}\tcount = {count}')
                    break
                elif total > k:
                    print(f'OVER')
                    break
                else:
                    print(f'i={i}, x={x}')
                    print(f'k={k},  total = {total},  count = {count}')

# The values for k, ranges, etc. are just experimental. Functions seems to work, but Success is rare.
try1 = Solution()
print(try1.randomArray())
try1.subarraySum(try1.randomArray(), 500)