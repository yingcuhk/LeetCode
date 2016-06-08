class Solution(object):
    """
    Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?
    """
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        H = len(citations)
        hInd = 0
        #hList = [lambda k: citations[k] -(H-k) for k in xrange(H)]

        while(hInd < H):
            if citations[H-hInd-1] < hInd+1:
                break
            hInd += 1
            
        return hInd