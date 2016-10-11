"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

https://leetcode.com/problems/letter-combinations-of-a-phone-number/


Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        Dict = [[" "],["*"], ["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
        
        #inds = [int(x) for x in digits]
        
        output = Dict[int(digits[0])]
        
        for k in range(1,len(digits)):
            temp = Dict[int(digits[k])]
            output = [x + z for x in output for z in temp]
        
        return output