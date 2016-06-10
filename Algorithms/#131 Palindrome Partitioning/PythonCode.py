"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution(object):
    
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return self.recursivePartition(s)
    
    def recursivePartition(self,s):
        L = len(s)
        Set = []
        for k in range(1,L+1):
            curstr = s[:k]
            
            if self.isPalindrome(curstr):
                remainstr = s[k:]
                if len(remainstr) == 0:
                    Set.append([curstr])
                    continue
                partitionset = self.recursivePartition(remainstr)
                            
                for partition in partitionset:
                    Set.append([curstr] + partition)
        return Set 


    def isPalindrome(self,s):
        
        L = len(s)
        for k in xrange(L/2):
            if s[k] != s[L-k-1]:
                return False
        return True