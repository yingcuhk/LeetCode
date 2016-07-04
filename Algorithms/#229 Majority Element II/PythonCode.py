"""
Given an integer array of size n, find all elements that appear more than ? n/3 ? times. The algorithm should run in linear time and in O(1) space.

My code is based on a pretty famous paper: Karp, Richard M., Scott Shenker, and Christos H. Papadimitriou. "A simple algorithm for finding frequent elements in streams and bags." ACM Transactions on Database Systems (TODS) 28.1 (2003): 51-55.

Similar results appear in several papers before. 

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        Dict = {} # a dict with 3 entries 
        
        # firstly find the candidate elements by checking the array once
        for num in nums:
            
            if num in Dict:
                Dict[num] += 1
            else:
                if len(Dict) < 3:
                    Dict[num] = 1
                else:
                    update = False
                    for key in Dict:
                        if Dict[key] <= 0:
                            del Dict[key]
                            Dict[num] = 1
                            update = True
                            break
                    if not update:
                        for key in Dict:
                            Dict[key] -= 1
        #print Dict
        
        # determine its exact frequency by another time of checking 
        
        for key in Dict:
            Dict[key] = 0
        for num in nums:
            if num in Dict:
                Dict[num] += 1.0
        #print Dict
        returnList = []
        L = len(nums)
        for key in Dict:
            if Dict[key]/L > 1/3.0:
                returnList.append(key)
                
        
        return returnList
