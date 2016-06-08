"""
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        keys = list(set(nums))
        NumLists = list([0]*len(keys))
        for num in nums:
            NumLists[keys.index(num)] += 1
        
        Ind = sorted(range(len(NumLists)), key=lambda x: NumLists[x], reverse=True)[:k]
        ans = [keys[ind] for ind in Ind]
        
        return ans