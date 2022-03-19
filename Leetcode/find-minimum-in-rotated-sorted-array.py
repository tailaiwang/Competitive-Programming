#Find Minimum in Rotated Sorted Array
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#Medium (Algorithms II), 19/03/2022
#Tailai Wang

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r = len(nums) - 1
        l = 0
        if len(nums) == 1:
            return nums[0]
        if nums[r] > nums[0]:
            return nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
            