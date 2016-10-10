"""

The set [1,2,3,бн,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note: Given n will be between 1 and 9 inclusive.
"""

from math import factorial
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k = k-1
        L = [l for l in range(1,n+1)]
        S = ""
        for l in xrange(n):
            base = factorial(n-l-1)
            ind = k // base
            k = k % base
            S += str(L[ind])
            L.remove(L[ind])
            

        
        return S