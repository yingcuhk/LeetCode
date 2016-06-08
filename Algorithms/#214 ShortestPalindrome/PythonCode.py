
class Solution(object):
    """
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
    """
    def shortestPalindrome(self, s):
        lenS,res = len(s),""
        if lenS <= 1: return s
        minStart, maxLen, i = 0, 1, 0
        while i < lenS:
            if lenS - i <= maxLen / 2: break
            j, k = i, i
            while k < lenS - 1 and s[k] == s[k + 1]: k += 1
            i = k + 1
            while k < lenS - 1 and j and s[k + 1] == s[j - 1]:  
                k, j = k + 1, j - 1
            if k - j + 1 >= maxLen and (j == 0): 
                minStart, maxLen = j, k - j + 1
        temp = s[minStart + maxLen:lenS]
        temp = temp[::-1]
        res = temp + s
        return res