"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        ### recursive solution        
        
        nums = [i for i in range(1,n+1)]
        return self.comb_constant_len(nums,k)
        #return Subsets
    def comb_constant_len(self,nums,k):
        L = len(nums)
        if k == 0 or k > L:
            return []
        if k == L:
            return [nums]
        if k == 1:
            return [[num] for num in nums]
            
        List1 = self.comb_constant_len(nums[1:],k-1)
        num = [nums[0]]
        List1 = [num+List for List in List1]
        if k <= L-1:
            List2 = self.comb_constant_len(nums[1:],k)
        else:
            List = []
        return List1 + List2
        
        