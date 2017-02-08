"""
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Subscribe to see which companies asked this question.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        return str(x)[::-1] == str(x)