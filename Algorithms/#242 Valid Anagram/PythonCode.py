"""
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}
        
        for c in s:
            if c in s_dict:
                s_dict[c] = s_dict[c] + 1
            else:
                s_dict[c] = 1
                
        for c in t:
            if c in t_dict:
                t_dict[c] = t_dict[c] + 1
            else:
                t_dict[c] = 1
        if len(s_dict) != len(t_dict):
            return False
        for c in s_dict:
            if c not in t_dict or s_dict[c] != t_dict[c]:
                return False
        return True
                
        """
        T = [c for c in t]
        for c in s:
            if c not in T:
                return False
            T.remove(c)
            
        return len(T) == 0
        """