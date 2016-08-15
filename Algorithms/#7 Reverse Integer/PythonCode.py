"""

Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        newx = x*(1-2*(x<=0))
        newx = int(str(newx)[::-1])

        """
        if x < 0:
            marker = -1
        else:
            marker = 1
        x = marker*x
        newx = x % 10
        x = x/10
        while x > 0:
            newx = newx * 10 + x%10
            x = x/10
        
        """
        if newx > 2147483647:
            return 0
        return newx * (1-2*(x<=0))
            