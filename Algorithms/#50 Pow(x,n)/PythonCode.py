
# Implement pow(x, n).

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n > 0:
            return self.recursive(x,n)
        else:
            return 1.0/self.recursive(x,-1*n)
    
    def recursive(self,x,n):
        
        if n == 1:
            return x
        if n == 0:
            return 1
            
            
        if n%2 == 0:
            v = self.recursive(x,n/2)
            return v*v
        else:
            v = self.recursive(x,(n+1)/2)
            return v*v/x
            
        
            