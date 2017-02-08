class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        self.height = height
        #return self.exhaustedSearch(height)
        CandPos,flag = self.filteredCandidates()
        max_vol = 0
        #print CandPos, flag
        if flag:
            for k1 in range(len(height)-1):
                for k2 in CandPos:
                    if k2 <= k1:
                        continue
                    max_vol = max(max_vol,min(height[k1],height[k2])*(k2-k1))
            return max_vol
        else:
            k1 = len(height)-1
            while k1 > 0:
                for k2 in CandPos:
                    if k2 >= k1:
                        continue 
                    max_vol = max(max_vol,min(height[k1],height[k2])*(k1-k2))
                k1 -= 1
            return max_vol
            


    def filteredCandidates(self):
        
        TempH = list(self.height)
        
        CandPos1 = []
        CandPos2 = []
        start = 0
        L = len(TempH)
        End = L
        while start < L and End > 0:
            temp = TempH[start:]
            max_index1 = temp.index(max(temp))
            #max_index1, _ = max(enumerate(TempH[start:]), key=lambda x: x[1])
            CandPos1.append(max_index1 + start)
            start = CandPos1[-1]+1
            
            temp = TempH[:End]
            max_index2 = temp.index(max(temp))
            #max_index2, _ = max(enumerate(TempH[:End]), key=lambda x: x[1])
            CandPos2.append(max_index2)
            End = max_index2

        if start >= L:
            return CandPos1, True
        else:
            return CandPos2, False
            
    def exhaustedSearch(self, height):

        max_vol = 0
        for k1 in range(len(height)-1):
            for k2 in range(k1+1, len(height)):
                vol = min(height[k1],height[k2])*(k2-k1)
                if vol > max_vol:
                    max_vol = vol
                    
        return max_vol