"""

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
      
        low = 1
        high = num // 2
        
        while low < high-1:
            mid = (low+high) // 2
            temp = mid * mid
            if temp > num:
                high = mid
            elif temp < num:
                low = mid
            else:
                return True
        if low*low == num or high*high == num:
            return True
        else:
            return False