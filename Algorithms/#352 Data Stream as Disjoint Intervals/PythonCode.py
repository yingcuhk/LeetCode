"""

Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of disjoint intervals.

For example, suppose the integers from the data stream are 1, 3, 7, 2, 6, ..., then the summary will be:

[1, 1]
[1, 1], [3, 3]
[1, 1], [3, 3], [7, 7]
[1, 3], [7, 7]
[1, 3], [6, 7]
Follow up:
What if there are lots of merges and the number of disjoint intervals are small compared to the data stream's size?
"""


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class SummaryRanges(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.heads = []
        self.tails = []

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        Flag, index = self.isInIntervals(val)
        H = self
        if not Flag:
            H = self.heads
            T = self.tails
            self.heads = H[:index] + [val] + H[index:]
            self.tails = T[:index] + [val] + T[index:]
            """
            print "***************************"
            print "#################"
            print self.heads
            print self.tails
            print "#################"
            """
            self.MergeIntervals()
            """
            print "#################"
            print self.heads
            print self.tails
            print "#################"
            print "***************************"
            """
    def MergeIntervals(self):
        N = len(self.heads)
        newHeads = []
        newTails = []
        for k in xrange(N):
            if k == N-1 or self.tails[k] + 1 < self.heads[k+1]:
                newHeads.append(self.heads[k])
                newTails.append(self.tails[k])
            else:
                self.heads[k+1] = self.heads[k]
                
        self.heads = newHeads
        self.tails = newTails
            
            
    def isInIntervals(self,val):
        
        for k, head in enumerate(self.heads):
            if val == head:
                return True, -1
            elif val > head:
                if val <= self.tails[k]:
                    return True, -1
            else:
                return False, k
                
        return False, len(self.heads)
        


    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        Intervals = [[x,y] for (x,y) in zip(self.heads,self.tails)]
        return Intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

