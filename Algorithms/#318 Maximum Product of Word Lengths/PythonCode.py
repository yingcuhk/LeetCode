class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
        Indicaters = list([0]*len(words))
        lenList = list([0]*len(words))
        for k,word in enumerate(words):
            val = 0
            for letter in word:
                val = val | (1 << (ord(letter)-ord('a')))
            Indicaters[k] = val
            lenList[k] = len(word)
            
        prod = 0
        for k1 in range(0,len(words)-1):
            for k2 in range(k1+1,len(words)):
                if Indicaters[k1] & Indicaters[k2] == 0:
                    prod = max(prod, lenList[k1]*lenList[k2])
        return prod
        
        """  # a simple solution by loop
        self.setList = list([0]*len(words)) 
        self.lenList = list([0]*len(words))
        for k,word in enumerate(words):
            self.setList[k] = set(word)
            self.lenList[k] = len(word)
        prod = 0
        for k1 in range(0,len(words)-1):
            set1 = self.setList[k1]
            for k2 in range(k1+1,len(words)):
                set2 = self.setList[k2]
                if len(set1.intersection(set2)) == 0:
                    prod = max(prod, self.lenList[k1]*self.lenList[k2])
                    
        return prod
        """
        
        """
        return self.recursiveSolution(0,len(words)-1)
        
    def recursiveSolution(self,beg, end):
        #print beg,end
        if end <= beg:
            return 0
        divPos=  (beg+end)//2
        #print "mid", divPos
        prod1 = self.recursiveSolution(beg,divPos)
        prod2 = self.recursiveSolution(divPos+1,end)
        
        prod = 0
        
        for k1 in range(beg,divPos+1):
            for k2 in range(divPos+1,end+1):
                if len(self.setList[k1].intersection(self.setList[k2])) == 0:
                    prod = max(prod, self.lenList[k1]*self.lenList[k2])

        return max(prod1,prod2,prod)
        """