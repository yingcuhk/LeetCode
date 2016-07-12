"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < = 5:
            return True
        if num <= 0:
            return False
        
        temp = num
        while temp %2 == 0:
            temp = temp/2
        while temp%3 == 0:
            temp = temp/3
        while temp%5 == 0:
            temp = temp/5
        
        return not temp > 1
            