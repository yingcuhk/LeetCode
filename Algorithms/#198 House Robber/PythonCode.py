
"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N == 0:
            return 0
        maxval_include_cur = list([0]*N)
        maxval_exclude_cur = list([0]*N)
        maxval_include_cur[0] = nums[0]
        for k in range(1,len(nums)):
            maxval_include_cur[k] = maxval_exclude_cur[k-1] + nums[k]
            maxval_exclude_cur[k] = max(max(maxval_include_cur[:k]),max(maxval_exclude_cur[:k]))
        
        #print maxval_include_cur
        #print maxval_exclude_cur
        return max(maxval_exclude_cur[-1],maxval_include_cur[-1])
            
        
        
        #return self.recursive_rob(nums,0)

    """
    # a simple recursive solution exceeding the time limit    
    def recursive_rob(self,nums,beg):
        if len(nums) == beg:
            return 0
        if len(nums) == beg+1:
            return nums[-1]
        
        # select the first one or not
        
        exclude1st = self.recursive_rob(nums,beg+1)
        include1st = nums[beg] + self.recursive_rob(nums,beg+2)
        
        if exclude1st > include1st:
            return exclude1st
        else:
            return include1st
    """