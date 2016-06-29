"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        L = len(s)
        if L <= 1:
            return L
        maxL = 0
        
        remains = s
        nextstart = 0
        while nextstart < L:
            if nextstart == L-1:
                curL = 1
                maxL = max(maxL,curL)
                nextstart = L
            Dict = {} 
            Dict[s[nextstart]] = nextstart
            curL = 1
            for k in xrange(nextstart+1,L):
                if s[k] in Dict:
                    maxL = max(maxL,curL)
                    nextstart = Dict[s[k]]+1
                    break
                else:
                    curL += 1
                    Dict[s[k]] = k
                    
            if k == L-1:
                maxL = max(maxL,curL)
                nextstart = L
            if L-nextstart < maxL:
                nextstart = L
            
        return maxL

        
        