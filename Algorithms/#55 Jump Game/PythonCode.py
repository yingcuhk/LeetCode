"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        L = len(nums)
        First_Reach_Area = 0
        old = 0
        new = 0
        Reached_Area_1_Jump = [t + nums[t] for t in range(len(nums))]
        while 1:
            new_reached = max(Reached_Area_1_Jump[old:new+1])
            
            if new_reached >= L-1:
                return True
            if new_reached <= new:
                break
            else:
                old = new+1
                new = new_reached
        
        return False
    """
    def sub_canJump(self, NUMs):
        # a recursive solution exceeding the time limitation 
        if NUMs[0] >= len(NUMs)-1:
            return True
        
        for k in range(1, len(NUMs)-1):
            if self.sub_canJump(NUMs[:k+1]) and self.sub_canJump(NUMs[k:]):
                return True
            
        return False
    """