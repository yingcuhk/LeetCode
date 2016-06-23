"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        words = s.split(" ")[::-1]
        
        reverse_s = ""
        for word in words:
            if len(word) > 0:
                reverse_s = reverse_s + word+" "
            
        return reverse_s[:-1]