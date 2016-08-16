class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        L = len(prices)
        
        profit1T = [0 for k in xrange(L)]
        
        minval = prices[0]
        for k in range(1,L):
            minval = min(minval,prices[k-1])
            profit1T[k] = max(profit1T[k-1], prices[k]-minval)
        
        profit2T = [0 for k in xrange(L)]
        profit2T[1] = max(profit1T[:2])
        temp = -1*prices[0]
        for k in range(2,L):
            temp = max(temp,profit1T[k-2] -prices[k-1])
            profit2T[k] = max(profit2T[k-1],profit1T[k], prices[k] + temp)
            
            
        return profit2T[-1]
        
        
        
        
        
""" an algorithm with complexity (n^2logn)
        self.price = prices    
        start = 0
        
        end = len(prices)-1
        
        val = self.maxProfitRecursion(start,end)
        for k in range(2,len(prices)-1):
            temp = self.maxProfitRecursion(start,k-1) + self.maxProfitRecursion(k,end)
            val = max(val,temp)
        return val
        
        
    def maxProfitRecursionOneTransaction(self,start,end):
        
        if end-start == 1:
            temp = max(self.price[end]-self.price[start],0)
            return temp
        if end <= start:
            return 0
            
        
        mid = (start+end)/2
        
        low_first_half = min(self.price[start:mid])
        high_second_half = max(self.price[mid:end+1])
        
        profit0 = high_second_half-low_first_half
        profit1 = self.maxProfitRecursion(start,mid-1)
        profit2= self.maxProfitRecursion(mid,end)
        
        
        onetrans = max(profit0,max(profit1,profit2))
       
        return onetrans 
        
  """     
        
        
        
        