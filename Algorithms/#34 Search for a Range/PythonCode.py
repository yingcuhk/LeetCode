"""
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].

"""




class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        L = len(nums)
        start = [0,L-1]
        ending = [0,L-1]
        
        return self.recursiveSolution(nums,target,start,ending)
        
    def recursiveSolution(self,nums,target,start,ending):
        
        flag1 = False
        if start[0] == start[1]:
            if nums[start[0]] == target:
                flag1 = True
                newstart = start
            else:
                return [-1,-1]
        else:
            startmid = int((start[0]+start[1])/2)
            if startmid == start[0]:
                if nums[start[0]] < target and nums[start[1]] == target:
                    newstart = [start[1],start[1]]
                else:
                    newstart = [start[0],start[0]]
            if nums[startmid] >= target:
                newstart = [start[0],startmid]
            else:
                newstart = [startmid+1,start[1]]
        flag2 = False
        if ending[0] == ending[1]:
            if nums[ending[0]] == target:
                flag2 = True
                newending = ending
            else:
                return [-1,-1]
        else:
            endingmid = int((ending[0]+ending[1])/2)
            if endingmid == ending[0]:
                if nums[ending[0]] == target and nums[ending[1]] > target:
                    newending = [ending[0],ending[0]]
                else:
                    newending = [ending[1],ending[1]]
            else:
                if nums[endingmid] <= target:
                    newending = [endingmid,ending[1]]
                else:
                    newending = [ending[0],endingmid-1]
        if flag1 and flag2:
            return [start[0], ending[0]]
        return self.recursiveSolution(nums,target,newstart,newending)
        
    
        
        
        
        
        
        
        
        
        
        