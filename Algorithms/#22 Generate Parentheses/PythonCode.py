
"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        strset = []
        for k in xrange(0,n): # k is inside ( ) and n-k is outside, k >=0 n-k >= 0
           strin = self.generateParenthesis(k)
           strappend = self.generateParenthesis(n-k-1)
           
           for str1 in strin:
               for str2 in strappend:
                   curstr = "("+str1+")"+str2
                   strset.append(curstr)
                   
        return strset
                   
                   
            
            
            
        