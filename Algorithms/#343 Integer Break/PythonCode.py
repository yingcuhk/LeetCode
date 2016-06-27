import math

"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).

Note: you may assume that n is not less than 2.

Show Hint 


"""
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        seg = int(n/math.exp(1))
        if seg <= 1:
            seg = 2
            return self.maxMul(n,seg)
        mul0 = 1
        if seg >= 3:
            mul0 = self.maxMul(n,seg-1)
        mul1 = max(self.maxMul(n,seg),mul0)
        mul2 = self.maxMul(n,seg+1)
        
        return max(mul1,mul2)
        

    def maxMul(self,n,seg):
        
        val1 = int(n/seg)
        rem = n-seg*val1
        
        mul = 1
        for k in range(0,seg):
            if k < rem:
                mul = mul*(val1+1)
            else:
                mul = mul*(val1)
                
        return mul
        
            