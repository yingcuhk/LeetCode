# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
"""
class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix

        M = len(self.matrix)
        if M == 0:
            self.SUM = [[]]
            return 
        N = len(self.matrix[0])
        if N == 0:
            self.SUM = [[]]
            return

        self.SUM = [[0 for n in xrange(N+1)] for m in xrange(M+1)]
        for m in range(1,M+1):
            for n in range(1,N+1):
                self.SUM[m][n] = self.SUM[m-1][n]+self.SUM[m][n-1]+self.matrix[m-1][n-1] - self.SUM[m-1][n-1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        
        return self.SUM[row2+1][col2+1] - (self.SUM[row1][col2+1]+self.SUM[row2+1][col1]-self.SUM[row1][col1])
        
        

