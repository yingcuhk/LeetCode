"""
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        return self.recursiveSolution(nums)
    
    def recursiveSolution(self, nums):
        if len(nums) == 1:
            return [nums]
            
        num = nums[0]
        
        postpermps = self.recursiveSolution(nums[1:])
        
        permps = []
        for permp in postpermps:
            for k in xrange(len(permp)+1):
                newperm = permp[:k] + [num] + permp[k:]
                if newperm not in permps:
                    permps.append(newperm)


        return permps