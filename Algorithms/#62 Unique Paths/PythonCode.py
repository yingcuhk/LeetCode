"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

 The figure is on the web: https://leetcode.com/problems/unique-paths/
 
 
How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

"""


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        Nums = [[0 for h in xrange(n)] for v in xrange(m)]
        
        for v in xrange(m):
            for h in xrange(n):
                if v == 0 or h == 0:
                    Nums[v][h] = 1
                else:
                    Nums[v][h] = Nums[v-1][h] + Nums[v][h-1]

        
        return Nums[m-1][n-1]