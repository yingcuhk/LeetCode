"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution(object):
    def permuteUnique(self, nums):
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
        
       