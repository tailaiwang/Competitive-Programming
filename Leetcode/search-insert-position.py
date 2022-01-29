#Search Insert Position
#https://leetcode.com/problems/search-insert-position/
#Easy, 28/01/2022
#Tailai Wang


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            cur = nums[mid]
            if cur == target:
                return mid
            if cur < target:
                low = mid + 1
            else:
                high = mid - 1
        return low
