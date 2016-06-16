"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
"""
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        M = len(nums1)
        N = len(nums2)
        
        if (N+M)%2 == 0:
            K1 = (M+N)/2
            K2 = (M+N)/2 + 1
            val1 = self.find_k_Largest(nums1,nums2,K1)
            val2 = self.find_k_Largest(nums1,nums2,K2)
            return (val1+val2)/2.0
        else:
            K = (M+N-1)/2+1
            return self.find_k_Largest(nums1,nums2,K)
            
    def find_k_Largest(self,nums1,nums2,k):
        """
        if len(nums1) > k:
            nums1 = list(nums1[:k])
        if len(nums2) > k:
            nums2 = list(nums2[:k])
        """
        L1 = len(nums1)
        L2 = len(nums2)

        if L1 == 0:
            return nums2[k-1]
        if L2 == 0:
            return nums1[k-1]

        if L1 + L2 == k:
            return max(nums1[-1],nums2[-1])
        if k == 1:
            return min(nums1[0],nums2[0])
            
        
        k1 = min(max(k/2,k-L2),L1)  # k1 >= 1 k1 and k2 are the kth, not the index
        # to ensure that k1 <= L1, k2 <= L2
        k2 = k-k1
        a = nums1[k1-1]
        b = nums2[k2-1]
        
        if a == b:
            return a
        elif a>b:
            return self.find_k_Largest(nums1[:k1],nums2[k2:],k-k2)
        elif a<b:
            return self.find_k_Largest(nums1[k1:],nums2[:k2],k-k1)
            