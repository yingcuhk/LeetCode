class Solution(object):
    """
    Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,
Given:
s1 = "aabcc",
s2 = "dbbca",

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
    """
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1)+len(s2) != len(s3):
            return False
        """  # solution by recursive, but with high complexity 
        if s1 == "":
            return s2 == s3
        if s2 == "":
            return s1 == s3
            
        F1 = False
        F2 = False
        if s1[0] == s3[0]:
            F1 = self.isInterleave(s1[1:],s2,s3[1:])
        if s2[0] == s3[0]:
            F2 = self.isInterleave(s1,s2[1:],s3[1:])
        return F1 or F2
        """
        if s1+s2 == s3 or s2+s1 == s3: # fast check, but is redudant 
            return True
        if s1 == "" or s2 == "" or s3 == "":
            return s1+s2 == s3
        # in the following, all strings have positive lengths 
        M = len(s1)
        N = len(s3)
        # create a Table to indicate whether s3[:n] can be formed by the interleaving of s1[:m] and s2[:n-m]
        Table = [False for k in xrange(N)]
        Table = [list(Table) for k in xrange(M)]
        for n in xrange(N): # m,n both start from 0
            for m in range(0,min(n+1,M)): # n is the length of s3 in the subpproblem
                # the following code is to checek whether Table[m,n] is true or not
                if len(s2) < n-m:
                    continue
                if m == 0:
                    if s2[:n] + s1[0] == s3[:n+1]:
                        Table[m][n] = True
                        continue
                else:
                    if Table[m-1][n-1] and s1[m] == s3[n]:
                        Table[m][n] = True
                        continue
                for k in range(m,n):
                    if Table[m][k]: # 
                        if s2[k-m:n-m] == s3[k+1:n+1]:
                            Table[m][n] = True
                            break
                
        return Table[-1][-1]
        
        
        