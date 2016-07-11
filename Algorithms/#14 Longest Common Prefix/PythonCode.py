"""
Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        tmp = reduce(self.longestCommonPrefix2,strs)
       
        return tmp
    def longestCommonPrefix2(self,str1,str2):
        ans = ""
        
        for k in xrange(min(len(str1),len(str2))):
            if str1[k] == str2[k]:
                ans = ans+str1[k]
            else:
                break
        return ans