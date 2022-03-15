#Arithmetic Slices
#https://leetcode.com/problems/arithmetic-slices/
#Medium (Daily Challenge), 03/03/2022
#Tailai Wang

class Solution(object):
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curDiff = -1
        count = 0
        retVal = 0
        for i in range(1, len(nums)):
            newDiff = nums[i] - nums[i-1]
            if newDiff != curDiff:
                curDiff = newDiff
                count = 1
            else:
                retVal += count
                count += 1
        return retVal
                
        
                                    
