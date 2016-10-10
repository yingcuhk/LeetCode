"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.G = grid
        self.M = len(grid)
        self.N = len(grid[0])
        
        self.dist = [[-1 for n in xrange(self.N)] for m in xrange(self.M)]
        
        return self.path_recursive(0,0)
        
        
        
    """
    A simple recursive solution 
    """
    def path_recursive(self, x_pos,y_pos):
        
        val = self.G[x_pos][y_pos]
        
        
        if x_pos == self.M-1 and y_pos == self.N-1:
            return val
        elif x_pos == self.M-1:
            return val + sum(self.G[x_pos][y_pos+1:])
        elif y_pos == self.N-1:
            for k in range(x_pos+1, self.M):
                val += self.G[k][-1]
            return val
        else:
            if self.dist[x_pos+1][y_pos] == -1:
                cand1 = self.path_recursive(x_pos+1, y_pos)
            else:
                cand1 = self.dist[x_pos+1][y_pos]
            if self.dist[x_pos][y_pos+1] == -1:
                cand2 = self.path_recursive(x_pos, y_pos+1)
            else:
                cand2 = self.dist[x_pos][y_pos+1]
            
            self.dist[x_pos][y_pos] = val + min(cand1, cand2)
            return val + min(cand1, cand2)


        
        
        
        