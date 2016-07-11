"""
Given two numbers represented as strings, return multiplication of the numbers as a string.

Note:
The numbers can be arbitrarily large and are non-negative.
Converting the input string to integer is NOT allowed.
You should NOT use internal library such as BigInteger.

"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 =='0':
            return '0'
        
        
        L1 = len(num1)
        L2 = len(num2)
        if L1 <= L2:
            L = L2
        else:
            temp = num1
            num1 = num2
            num2 = temp
            L = L1
        
        #L = len(num2)
        ans = "0"
        ADD0 = ""
        self.Dict = {}
        for k in xrange(L):
            pos=  L-1-k
            cha = num2[pos]
            temp = self.subintegermultiply(num1,cha)
            ans = self.integerssum(temp+ADD0,ans)
            ADD0 = ADD0 +'0'
        
        return ans
        
    
    def subintegermultiply(self,num1,num2):
        #num1 is a string , nums is a character
        
        if num2 == '0':
            return '0'
        if num2 in self.Dict:
            return self.Dict[num2]
        ans = ''
        t2 = int(num2)
        add = 0
        for c in num1[::-1]:
            temp = t2*int(c)+add
            val = temp%10
            ans = str(val)+ans
            add = temp // 10

        if add > 0:
            ans = str(add)+ans
        self.Dict[num2] = ans
        
        return ans
            
    def integerssum(self,nums1,nums2):
        L1 = len(nums1)
        L2 = len(nums2)
        if L1 < L2:
            nums1 = '0'*(L2-L1) + nums1
        if L1 > L2:
            nums2 = '0'*(L1-L2) + nums2
        add = 0
        L = max(L1,L2)
        ans = ""
        for k in xrange(L):
            pos=  L-1-k
            val1 = int(nums1[pos])
            val2 = int(nums2[pos])
            temp = (val1+val2 + add)
            val = temp%10 
            ans = str(val)+ans
            add = temp // 10
            
        if add == 1:
            ans = '1' + ans
            
        return ans