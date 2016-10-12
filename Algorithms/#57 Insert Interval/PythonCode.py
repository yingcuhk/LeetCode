"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        self.H = []
        self.T = []
        for interval in intervals:
            self.H.append(interval.start)
            self.T.append(interval.end)
            
        self.insertOnly(newInterval)
        self.merge()
        
        INTERVALS = [Interval(x,y) for (x,y) in zip(self.H,self.T)]
        
        return INTERVALS
    def insertOnly(self, newInterval):
        
        h = newInterval.start
        t = newInterval.end
        if len(self.H) == 0:
            self.H = [h]
            self.T = [t]
            return
        
        k = 0
        flag = False
        while k < len(self.H):
            if self.H[k] >= h:
                self.H = self.H[:k] + [h] + self.H[k:]
                self.T = self.T[:k] + [t] + self.T[k:]
                flag = True
                break
            k += 1
        if not flag:
            self.H = self.H + [h]
            self.T = self.T + [t]

        
    def merge(self):
        
        newH = []
        newT = []
        
        for k in xrange(len(self.H)-1):
            if self.T[k] < self.H[k+1]:
                newH.append(self.H[k])
                newT.append(self.T[k])
            else:
                self.H[k+1] = self.H[k]
                if self.T[k+1] < self.T[k]:
                    self.T[k+1] = self.T[k]
                    
        newH.append(self.H[-1])
        newT.append(self.T[-1])
        
        self.H = newH
        self.T = newT
        
