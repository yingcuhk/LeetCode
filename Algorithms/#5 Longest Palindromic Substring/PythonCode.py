"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"

"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.L = len(s)
        start = 0
        end = 0
        max_L = 1
        for k in range(self.L):
            L1 = self.type1Palindromic(k)
            L2 = self.type2Palindromic(k)
            if max(2*L1+1,2*L2) <= max_L:
                continue
            if 2*L1+1 > 2*L2:
                start = k-L1
                end = k+L1
                max_L = 2*L1+1
            else:
                start = k-L2+1
                end = k+L2
                max_L = 2*L2
            
            
        return s[start:end+1]
    def type1Palindromic(self, k):
        # abcba
        L = 0
        while True:
            start = k-L-1
            end = k+L+1
            if start >=0 and end < self.L and self.s[start] == self.s[end]:
                L += 1
            else:
                break
        return L
    def type2Palindromic(self, k):
        # bb
        L = 0
        while True:
            start = k-L
            end = k+L+1
                
            if start >=0 and end < self.L and self.s[start] == self.s[end]:
                L += 1
            else:
                break
        return L
        
"""        
        Candidates = {}
        L = len(s)
        for k in range(L):
            Candidates[k] = 0
        
        end_Flag = False 
        while not end_Flag:
            max_val = 0
            end_Flag = True 
            for k in Candidates:
                start = k - Candidates[k]-1
                end = k + Candidates[k]+1
                
                if start >=0 and end < L and s[start] == s[end]:
                    Candidates[k] += 1
                    end_Flag = False
                
                max_val = max(Candidates[k],max_val)
            
            cands = Candidates.keys()
            for k in cands:
                if Candidates[k] < max_val:
                    del Candidates[k]
        k = Candidates.keys()[0]
        start = k - Candidates[k]
        end = k + Candidates[k]
        s1 =  s[start:end+1]
        
        Candidates = {}
        L = len(s)
        for k in range(L):
            Candidates[k] = 0
        
        end_Flag = False 
        while not end_Flag:
            max_val = 0
            end_Flag = True 
            for k in Candidates:
                start = k - Candidates[k]
                end = k + Candidates[k]+1
                
                if start >=0 and end < L and s[start] == s[end]:
                    Candidates[k] += 1
                    end_Flag = False
                
                max_val = max(Candidates[k],max_val)
            
            cands = Candidates.keys()
            for k in cands:
                if Candidates[k] < max_val:
                    del Candidates[k]
                    
        
        k = Candidates.keys()[0]
        start = k - Candidates[k]+1
        end = k + Candidates[k]
        s2 =  s[start:end+1]
        
        if len(s1) > len(s2):
            return s1
        else:
            return s2
"""
            
        