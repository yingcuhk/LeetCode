"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        if L <= 1:
            return L
        pos = 0
        for k in range(1,L):
            if nums[k] != nums[pos]:
                nums[pos+1] = nums[k]
                pos += 1
                
                
        return pos+1

