"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 ¡ú 1,3,2
3,2,1 ¡ú 1,2,3
1,1,5 ¡ú 1,5,1
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        L = len(nums)
        highcur = L-2
        lowcur = L-1
        Flag = False
        while highcur >= 0:
            cand = nums[highcur]

            for k in range(highcur+1,L):
                #print k,nums[k],nums[highcur]
                if nums[k] > nums[highcur]:
                    lowcur = k
                    Flag = True
                    
            if Flag:
                break
            highcur -= 1
        print Flag
        if Flag:
            temp = nums[highcur]
            nums[highcur] = nums[lowcur]
            nums[lowcur] = temp
            temp = nums[highcur+1:]
            temp = sorted(temp)
            nums[highcur+1:] = temp
        else:
            nums.sort()
        #return nums
        
                