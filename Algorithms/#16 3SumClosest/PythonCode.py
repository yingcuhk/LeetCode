
"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        D = abs(sum(nums[:3])-target)
        self.nums = sorted(nums)
        if self.isthreeSum0(target):
            return target
        for dist in range(1,D+1):
            
            if self.isthreeSum0(target-dist):
                return target-dist
            if self.isthreeSum0(target+dist):
                return target+dist
        
        
    def isthreeSum0(self,target):
        
        #nums = self.nums
        N = len(self.nums)
        for k in xrange(N-2):
            head = self.nums[k]
            start = k+1
            end = N-1
            
            while start < end:  
                
                a = self.nums[start]
                b = self.nums[end]
                flag = head + a + b
                if flag == target:
                    return True
                if flag > target :
                    end -= 1
                else:
                    start += 1
            
        return False
                
        
            
            
            
            