"""
Given a non negative integer number num. For every numbers i in the range 0 ¡Ü i ¡Ü num calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].
"""

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        k = 1
        flag = 0
        ind = 0
        while k <= num:
            if len(ans) >= 2**flag:
                flag += 1
                ind = 0
            ans.append(ans[ind]+1)
            ind+=1
            k += 1
            
        return ans