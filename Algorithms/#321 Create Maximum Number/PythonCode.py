
"""
Given two arrays of length m and n with digits 0-9 representing two numbers. Create the maximum number of length k <= m + n from digits of the two. The relative order of the digits from the same array must be preserved. Return an array of the k digits. You should try to optimize your time and space complexity.

Example 1:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
return [9, 8, 6, 5, 3]

Example 2:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
return [6, 7, 6, 0, 4]

Example 3:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
return [9, 8, 9]
"""


class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        S = [(0,0)]
        remain_k = k
        pos = []
        while remain_k > 0:
            new_S = []
            highdig = -1
            for s in S:
                canddig, state = self.highest_digit(nums1,nums2,s,remain_k)
                if canddig > highdig:
                    highdig = canddig
                    new_S = state
                if canddig == highdig:
                    new_S = list(set(new_S + state))
                
            #print new_S
            pos.append(highdig)
            S = new_S
            remain_k = remain_k-1
            
        return pos

        #return self.maxNum_recursive(nums1,nums2,0,0,k)
    
    def highest_digit(self,nums1,nums2,state,remain_k):
        
        beg1 = state[0]
        beg2 = state[1]
        N1 = len(nums1)
        N2 = len(nums2)
        if remain_k == 1:
            return max(nums1[beg1:]+nums2[beg2:]), [(N1,N2)]
        ind1,ind2 = beg1,beg2
        highdig1 = -1
        pos1 = -1
        while N1-ind1+N2-beg2 >= remain_k and ind1 < N1:
            if nums1[ind1] > highdig1:
                highdig1 = nums1[ind1]
                pos1 = ind1
            ind1 += 1
        highdig2 = -1
        pos2 = -1
        while N1-beg1+N2-ind2 >= remain_k and ind2 < N2:
            if nums2[ind2] > highdig2:
                highdig2 = nums2[ind2]
                pos2 = ind2
            ind2 +=1
                
        if highdig1 > highdig2:
            return highdig1, [(pos1+1,beg2)]
        elif highdig2 > highdig1:
            return highdig2, [(beg1, pos2+1)]
        else:
            return highdig1, [(pos1+1,beg2),(beg1, pos2+1)]
    
    """
    
    # a recursive solution
    def maxNum_recursive(self,nums1,nums2,beg1,beg2,k):
        
        N1 = len(nums1)
        N2 = len(nums2)
        
        if k == 0:
            return []
        
        highdig1 = -1
        pos1 = -1
        ind1,ind2 = beg1,beg2
        while N1-ind1+N2-beg2 >= k and ind1 < N1:
            if nums1[ind1] > highdig1:
                highdig1 = nums1[ind1]
                pos1 = ind1
            ind1 += 1
        highdig2 = -1
        pos2 = -1
        while N1-beg1+N2-ind2 >= k and ind2 < N2:
            if nums2[ind2] > highdig2:
                highdig2 = nums2[ind2]
                pos2 = ind2
            ind2 +=1
            
        if highdig1 > highdig2:
            return [highdig1]+self.maxNum_recursive(nums1,nums2,pos1+1,beg2,k-1)
        elif highdig2 > highdig1:
            return [highdig2]+self.maxNum_recursive(nums1,nums2,beg1,pos2+1,k-1)
        else:
            if pos2 == N2-1:
                return [highdig1]+self.maxNum_recursive(nums1,nums2,pos1+1,beg2,k-1)
            if pos1 == N1-1:
                return [highdig2]+self.maxNum_recursive(nums1,nums2,beg1,pos2+1,k-1)
            pos1 = [highdig1]+self.maxNum_recursive(nums1,nums2,pos1+1,beg2,k-1)
            pos2 = [highdig2]+self.maxNum_recursive(nums1,nums2,beg1,pos2+1,k-1)
            return self.the_larger_one(pos1,pos2)

    def the_larger_one(self,pos1,pos2):
        for val1,val2 in zip(pos1,pos2):
            if val1 > val2:
                return pos1
            if val2 > val1:
                return pos2

        return pos1
    """
    
    