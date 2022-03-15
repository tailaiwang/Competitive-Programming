#Single Number
#https://leetcode.com/problems/single-number/
#Easy (Daily Challenge), 15/02/2022
#Tailai Wang

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = Counter(nums)
        for num in nums:
            if nums[num] == 1:
                return num
        
