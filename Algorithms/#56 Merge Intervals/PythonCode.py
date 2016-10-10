"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervalL = [[x.start, x.end] for x in intervals]
        intervalList = sorted(intervalL, key = lambda x: x[0])
        H = [x[0] for x in intervalList]
        T = [x[1] for x in intervalList]
        
        newH = []
        newT = []
        
        for k in xrange(len(H)):

            if k < len(H)-1 and T[k] >= H[k+1]:
                H[k+1] = H[k]
                if T[k] > T[k+1]:
                    T[k+1] = T[k]
            else:
                newH.append(H[k])
                newT.append(T[k])
                
        intervals = [Interval(h,t) for (h,t) in zip(newH, newT)]
        
        return intervals
        
