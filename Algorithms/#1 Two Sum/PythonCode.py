"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        orinums = list(nums)
        nums.sort()
        head = 0 
        tail = len(nums)-1
        
        while head < tail:
            if nums[head] + nums[tail] > target:
                tail -= 1
            elif nums[head] + nums[tail] < target:
                head += 1
            else:
                break
        val1 = nums[head]
        val2 = nums[tail]
        if val1 == val2:
            inds = [k for k, val in enumerate(orinums) if val == val1]
            return [inds[0], inds[1]]
        else:
            return [orinums.index(nums[head]), orinums.index(nums[tail])]