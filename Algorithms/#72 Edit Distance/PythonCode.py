"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""



class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        if len(word1) == 0 or len(word2) == 0:
            return len(word1)+len(word2)
        
        N1 = len(word1)
        N2 = len(word2)
        Table = [[0 for m in xrange(N2+1)] for n in xrange(N1+1)]
        for k in range(1,N1+1):
            Table[k][0] = k
        for k in range(1,N2+1):
            Table[0][k] = k
        
        for n1 in range(1,N1+1):
            for n2 in range(1,N2+1):
                
                if word1[n1-1] == word2[n2-1]:
                    Table[n1][n2] = Table[n1-1][n2-1]
                else:
                    # delete the last vector of word1
                    T1 = 1 + Table[n1-1][n2]
                    # replace the last vector of word1
                    T2 = 1 + Table[n1-1][n2-1]
                    # insert a letter at the end of word1
                    T3 = 1 + Table[n1][n2-1]
                    Table[n1][n2] = min(T1,T2,T3)
        
                
        
        
        return Table[N1][N2]
        
        
        """
        return self.recursiveSolution(0,0,word1,word2)
        
        # a recursive solution, the codes are direct and intuitive, but exceeding the time limit. 
    def recursiveSolution(self,beg1,beg2,word1,word2):
        
        
        if beg1 == len(word1) or beg2 == len(word2):
            return len(word1)- beg1 + len(word1) - beg2
        
        if word1[beg1] == word2[beg2]:
            return self.recursiveSolution(beg1+1,beg2+1,word1,word2)

        # try to replace the first letter of word1 by the first letter of word2
        L1 = 1+ self.recursiveSolution(beg1+1,beg2+1,word1,word2)
        # try to delete the first letter of word1
        L2 = 1 + self.recursiveSolution(beg1+1,beg2,word1,word2)
        L = min(L1,L2)
        # try to insert the first letter of word2 in the front of word1
        L3 = 1 + self.recursiveSolution(beg1,beg2+1,word1,word2)
        L = min(L,L3)
        
        return L
        
        """
