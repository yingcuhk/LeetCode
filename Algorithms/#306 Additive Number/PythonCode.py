"""

Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.

For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.

1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199
Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Follow up:
How would you handle overflow for very large input integers?
"""

class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        
        L = len(num)
        if L <= 2:
            return False
        
        if num[0] == '0':
            val1s = [0]
        else:
            val1s = [int(num[:k]) for k in range(1,L-1)]

        string = num
        for k1, val1 in enumerate(val1s):
            if num[k1+1] == '0':
                val2s = [0]
            else:
                val2s = [int(num[k1+1:k2]) for k2 in range(k1+2,L)]
            #print val1, val2s
            for k2, val2 in enumerate(val2s):
                
                #print val1, val2, num[k1+k2:]
                if self.onePass(val1,val2,num[k1+1+k2+1:]):
                    return True

        return False
    
    def onePass(self, val1, val2, string):
        
        while len(string) > 0:
            Flag, newval, string = self.nextVal(val1,val2,string)
            if not Flag:
                return False
            else:
                val1 = val2
                val2 = newval
        return True
    def nextVal(self, val1, val2, string):
        if string[0] =='0':
            return False, -1, ""
        addnum = val1 + val2
        addstr = str(addnum)
        L = len(addstr)
        if len(string) < L:
            return False, -1, ""
        temp = string[:L]
        if temp == addstr:
            return True, addnum, string[L:]
        else:
            return False, -1, ""
