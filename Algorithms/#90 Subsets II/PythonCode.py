"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        L = len(nums)
        NumSets = 2**L
        Subsets = []
        for n in xrange(NumSets):
            indstr = bin(n)[2:].zfill(L)
            subset = []

            for x,y in zip(nums,indstr):
                if y == '1':
                    subset.append(x)
            subset = sorted(subset)
            if subset not in Subsets:
                Subsets.append(subset)
        
        return Subsets