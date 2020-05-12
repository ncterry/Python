"""
Give a sorted array of nums, remove duplicates so that each element only appears once.
Do not allocate extra space for another array. Modify in place.

nums1 = [1,1,2]
nums2 = [0,0,1,1,1,2,2,3,3,4]
    Should return, [0,1,2,3,4] with length=5
"""


class Solution:
    def removeDuplicates(self, nums):
        # type nums: List[int]
        # rtype: int
        if not nums:
            return 0

        count = 0
        print(nums)
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        print(nums)             # [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
        print(nums[0:count+1])  # [0, 1, 2, 3, 4]
        return count + 1        # 5


Q1 = Solution()
print(Q1.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
"""
Leads to this in the end:
    Original:       [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Final:          [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
    Return count:   5
    
The array has not changed in size, but we have the new array sorted in single order.
There are still extras on the end, but we also returned the new length of 5
So the system has the first 5 sorted in the new array, and we know how long we should look
        [0, 1, 2, 3, 4 .......]
"""