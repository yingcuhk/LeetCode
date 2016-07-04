"""

Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # a simple solution using binary serach 
        
        low = 0
        high = x
        
        while 1:
            mid = (low+high) // 2
            if mid**2 <= x:
                if (mid+1)**2 > x:
                    return mid
                else:
                    low = mid+1
                
            else:
                if (mid-1)**2 <= x:
                    return mid-1
                else:
                    high = mid
                    

        