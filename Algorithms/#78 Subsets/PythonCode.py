class Solution(object):
    """
    
    Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        L = len(nums)
        NumSets = 2**L
        Subsets = list([[]]*NumSets)
        for n in xrange(NumSets):
            indstr = bin(n)[2:].zfill(L)
            subset = []

            for x,y in zip(nums,indstr):
                if y == '1':
                    subset.append(x)
            Subsets[n] = subset
        
        return Subsets
        

    
    