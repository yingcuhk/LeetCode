"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""



class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [x for x in range(1,10)]
        #print nums
        return self.recursiveSolution(nums,k,n)
        
        
    def recursiveSolution(self, nums,k,n):
        
        if k > len(nums):
            return []
        if n == 0 or n > sum(nums[-1*k:]) or n < nums[0] or k == 0:
            return []
        if k == 1 and nums[0] == n:
            return [[nums[0]]]
        List1 = self.recursiveSolution(nums[1:],k,n) # do not select the first
        
        shortList2 = self.recursiveSolution(nums[1:],k-1,n-nums[0]) # select the first 
        
        List2 = []
        for shortl in shortList2:
            List2.append([nums[0]]+shortl)
            
        return List1+List2
        