"""
Given a positive integer n and you can do operations as follow:

If n is even, replace n with n/2.
If n is odd, you can replace n with either n + 1 or n - 1.
What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1
Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1
"""

class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.Dict = {}
        self.Dict[1] = 0
        self.Dict[2] = 1
        
        t = 1
        count = 0
        while t <= n:
            t = t*2
            count += 1
            self.Dict[t] = count
        #self.Dict[t] = count
        
        return self.recursiveSolution(n)
    """
        t = 1
        count = 0
        while t < n:
            count += 1
            t = t*2
        
        if t == n:
            return count
        sig = (t - n < n-t/2) # + if sig is True

        count = 0
        
        while n != 1:
            print n
            if n%2 == 0:
                n = n/2
            else:
                if sig:
                    n = n+1
                else:
                    n = n-1
            count += 1
            
        return count
        
    """
    
    def recursiveSolution(self, n):
            
        if n in self.Dict:
            return self.Dict[n]
        #print n
        cand = n-1
        if n%2 == 0:
            cand = min(cand,self.recursiveSolution(n/2)+1)
        else:
            cand = min(cand,self.recursiveSolution(n-1)+1)
            cand = min(cand,self.recursiveSolution(n+1)+1)
        
        self.Dict[n] = cand
        
        return cand
        
        
        
        
        
        
        
        
        