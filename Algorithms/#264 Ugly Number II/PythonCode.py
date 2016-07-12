"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note that 1 is typically treated as an ugly number.

"""



class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 5:
            return n
        UglyList = [1,2,3,4,5]
        UglyList += [0 for k in xrange(n-5)]
        #print UglyList
        K = 4
        while K < n-1:
            cur = UglyList[K] 
            
        
            temp = cur // 2 
            
            cand1 = self.ALargerUglyNum(temp,UglyList,K)*2
            temp = cur // 3
            cand2 = self.ALargerUglyNum(temp,UglyList,K)*3
            temp = cur // 5 
            cand3 = self.ALargerUglyNum(temp,UglyList,K)*5

            K += 1
            UglyList[K] = min(cand1,cand2,cand3)
        return UglyList[-1]
            
    def ALargerUglyNum(self,val,UglyList,K):
        
        beg = 0
        end = K
        
        pos = (beg+end) // 2
        
        while UglyList[pos] != val and end - beg > 1:
            
            if UglyList[pos] > val:
                end = pos
            else:
                beg = pos
            pos = (beg+end) // 2
            
        if UglyList[pos] == val:
            return UglyList[pos+1]
        if end-beg == 1:
            return UglyList[end]
        
        