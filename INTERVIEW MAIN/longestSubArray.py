"""
Given an array of numbers
Given a target sum.
    array = [2,4,7,9,8,3,6,4,2,1,0,1,8,4]
    sum = 12

Find the longest sub-array that = 12

8,4
6,4,2
2,1,0,1,8
They all are sequential sub-arrays that equal 12
Have program find the longest one.
"""


def longestSubArray(array, targetSum):
    left, right, total = 0, 0, 0    # left/right-most position in array
    list = [0,0,0]                  # [distance between left/right], left, right
    for n in range(0, len(array)):
        left = n                        # Left++ if sum=targetSum or sum > targetSum
        for x in range(n, len(array)):  # right should start at left --> , and never be BEFORE left
            right = x                   # right should always be == or > than left.
            total = total + array[right]
            if total == targetSum and (right - left + 1) > list[0]:  # Only log if this subArray-success is longer than.
                list[0] = right - left + 1  # Length of sub-Array success.
                list[1] = left
                list[2] = right
                print(f'T = {total}')
                print(f'Length of SubArray = {right-left+1}')
                for m in range(left, right+1):
                    print(f'\tarray[{m}] = {array[m]}')
                total = 0
                break
            elif total > targetSum:
                total = 0
                break


    return list
# -----------------------------------------------------------
list = longestSubArray(([2,10,7,9,8,3,6,4,2,1,0,1,8,7,2,5,1,0,6,9,3,5,2,4,1,0,3,6,7,3,5,1,1,1,1,1,1,1,1,1,1,2,7,9,3,5,4]),  12)
print(f'Longest subArray = {list[0]}'
      f'\nStart = {list[1]}'
      f'\nEnd   = {list[2]}')