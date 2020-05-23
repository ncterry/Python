"""
We have a list of numbers:  [5, 7, 2, 3, 4, 1, 6]
We want to return the 3rd largest number

    k=3     --> ..... 5, 6, 7   so 5 is what we need to return.

Iterate over is brute force     0(k*n)
Sort the array then return value at len(array)-k
    But just sorting itself is    0(nlogn)

We want to use the heap data structure, similar to binary tree.
            100
          19    36
        17 3   25 1
      2 7

We are going to for example, [5, 7, 2, 3, 4, 1, 6] take 6th, the last number
Then we go though and see if numbers are greater or less than 6
    sort them based on that.
    0(2n)
"""

# K-th Largest Number
# Video explanation at https://www.youtube.com/watch?v=QGVCnjXmrNg

class Solution(object):
  def findKthLargest(self, arr, k):
    left = 0                # left index in array
    right = len(arr) - 1    # right index in array
    while left <= right:
      pivotIndex = self._partition(arr, left, right)
      if pivotIndex == len(arr) - k:
        return arr[pivotIndex]
      elif pivotIndex > len(arr) - k:
        right = pivotIndex - 1
      else:
        left = pivotIndex + 1
    return -1

  def _partition(self, arr, low, high):
    pivot = arr[high]
    index = low
    for j in range(low, high):
      if arr[j] <= pivot:
        arr[index], arr[j] = arr[j], arr[index]
        index += 1
    arr[index], arr[high] = arr[high], arr[index]
    return index


print(Solution().findKthLargest([5, 7, 2, 3, 4, 1, 6], 3))
# 5
