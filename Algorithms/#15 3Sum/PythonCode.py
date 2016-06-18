"""
iven an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        # a better soltuion 
        
        ThreeSum = []
        nums = sorted(nums)
        
        for m in xrange(len(nums)-2):
            start = m+1
            end = len(nums)-1
            val = nums[m]
            while start < end:
                temp =  val + nums[start] + nums[end]
                if temp == 0:
                    candset = [val, nums[start],nums[end]]
                    if candset not in ThreeSum:
                        ThreeSum.append(candset)
                    start += 1 
                    end -= 1
                elif temp > 0:
                    end -= 1
                else:
                    start += 1
                    
        return ThreeSum
             
        
        
        
        
        """
        # naive solution with sorting 
        ThreeSum = []
        nums = sorted(nums)
        
        for m in xrange(len(nums)-2):
            for n in range(m+1,len(nums)-1):
                sum2 = nums[m]+nums[n]
                if -1*sum2 in nums[n+1:]:
                    temp = [nums[m],nums[n],-1*sum2]
                    if temp not in ThreeSum:
                        ThreeSum.append(temp)
                
            
        return ThreeSum
        """