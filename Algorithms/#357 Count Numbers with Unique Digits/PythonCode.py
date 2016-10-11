"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ¡Ü x < 10n.

Example:
Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ¡Ü x < 100, excluding [11,22,33,44,55,66,77,88,99])
"""


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.recursiveSolution(n)
        
        
    def recursiveSolution(self, n):
        if n == 0:
            return 1
        if n == 1:
            return 10
        """
        if n == 2:
            return 91
        """
        T = self.recursiveSolution(n-1)
        
        count = 9
        for k in xrange(n-1):
            count = count * (9-k)
        count += T
        return count