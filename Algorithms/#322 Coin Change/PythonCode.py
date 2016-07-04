"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
"""



class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        
        CountList = list([-1]*(amount+1))
        CountList[0] = 0
        
        for k in range(1,amount+1):
            
            count = -1
            for coin in coins:
                if k-coin < 0 :
                    continue
                if CountList[k-coin] >= 0:
                    if count == -1 or CountList[k-coin] + 1< count:
                        count = CountList[k-coin]+1
            CountList[k] = count
            
        return CountList[-1]
        # a simple recursive solution but exceeding the time limit
        """
        self.CountList = list([-1]*(amount+1))
        self.CountList[0] = 0
        return self.recursiveCoin(coins, amount)
        
    def recursiveCoin(self,coins,amount):
        #print amount, self.CountList
        if self.CountList[amount] >= 0:
            return self.CountList[amount]
        
        
        count = -1
        for k, coin in enumerate(coins):
            if amount < coin:
                nums = -1
            else:
                if self.CountList[amount-coin] >= 0:
                    nums = self.CountList[amount-coin] + 1
                else:
                    N = amount // coin
                    nums = -1
                    
                    temp = self.recursiveCoin(coins, amount-coin)
                    if temp >= 0:
                        nums = temp + 1
                        
            if nums >= 0:
                if count == -1 or nums < count:
                    count = nums
        
        self.CountList[amount] = count
        
        return count
            
        """
            
            
            
            
        