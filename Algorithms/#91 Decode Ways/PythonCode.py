"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

"""



class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0:
            return 0
            
        # a recursive solution 
        #Num,_ = self.recursiveNumDecodings(s)
        
        # nonrecursive solution 
        Num = self.nonrecursiveNumDecodings(s)
        return Num
        
        
    def recursiveNumDecodings(self,s):
        
        if len(s) == 1:
            if s == '0':
                return 0,1
            else:
                return 1,1 # ways of decoding the strings including the first letter or not
        L1,L2 = self.recursiveNumDecodings(s[1:])
        
        val12 = int(s[:2])
        if s[0] == '0':
            return 0,L1
        if val12 <= 26:
            L0 = L1 + L2
        else:
            L0 = L1

        return L0,L1
        
    def nonrecursiveNumDecodings(self,s):
        
        precount = 0
        curcount = 1
        lastletter = '9'
        
        for nextletter in s:
            
            if nextletter =='0':
                val = int(lastletter+nextletter)
                if val == 10 or val == 20:
                    nextcount = precount
                else:
                    return 0
            else:
                if lastletter == '0':
                    nextcount = curcount
                else:
                    val = int(lastletter+nextletter)
                    if val <= 26:
                        nextcount = curcount + precount
                    else:
                        nextcount = curcount
                
            
            precount = curcount 
            
            curcount = nextcount
            lastletter = nextletter
            
        return curcount
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        