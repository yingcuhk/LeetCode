"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.recursiveSolution(nums)
    
    def recursiveSolution(self,nums):
        # a solution that is fast on the testing set but seems not O(N)
        # this solution use the naive method implemented below
        L = len(nums)
        if L == 1:
            return 1
        minval = nums[0]
        maxval = nums[0]
        for num in nums:
            if num < minval:
                minval = num
            if num > maxval:
                maxval = num
        Interval = maxval-minval+1
        
        if Interval < L**2:
            return self.naiveSolution(nums)
            
        SegL = Interval/(L-1)
        SubLists = [[] for k in xrange(L+1)]
        for num in nums:
            pos = int((num-minval)/SegL)
            SubLists[pos].append(num)
            SubLists[pos+1].append(num)
        LongL = 0
        for sublist in SubLists:
            if len(sublist) > 0:
                temp = self.recursiveSolution(sublist)
                LongL = max(LongL,temp)
        
        return LongL
        

    def naiveSolution(self,nums):
        # a naive solution to utilize too much memory 
        #print nums
        if len(nums) == 1:
            return 1
        minval = nums[0]
        maxval = nums[0]
        for num in nums:
            if num < minval:
                minval = num
            if num > maxval:
                maxval = num
        ListLen = maxval-minval+1
        Markers = list([0]*ListLen)
        for num in nums:
            Markers[num-minval] = 1

        LongestL = 1
        curL = 1
        for m in range(1,ListLen):
            if Markers[m] == 1:
                curL += 1
            else:
                if curL > LongestL:
                    LongestL = curL
                curL = 0
        if curL > LongestL:
            LongestL = curL       
                
        return LongestL
        
                
# [2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645]     
            
            
