
"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""

# SOLUTION
"""

We firstly construct a directed and acyclic graph and then compute the longest path in this graph.

"""
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L = len(nums)
        if L == 0 or L == 1:
            return L
        preNodes = [[] for k in xrange(L)]
        
        # to construct the directed and acyclic graph
        for k in xrange(L-1):
            for v in range(k+1,L):
                if nums[k] < nums[v]:
                    preNodes[v].append(k)
        Long_to_cur = [0 for k in xrange(L)]
        for k in xrange(L):
            preLong = 0
            for prenode in preNodes[k]:
                preLong = max(preLong,Long_to_cur[prenode])
                
            Long_to_cur[k] = preLong+1
            
        return max(Long_to_cur)
        
        