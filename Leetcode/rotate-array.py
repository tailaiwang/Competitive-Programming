<<<<<<< HEAD
#Rotate Array
#https://leetcode.com/problems/rotate-array/
#Medium (Daily Challenge), 29/01/2022
#Tailai Wang


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        spots = k % n
        nums[:] = nums[(n - spots):] + nums[:(n - spots)]
=======
#Rotate Array
#https://leetcode.com/problems/rotate-array/
#Medium (Daily Challenge), 29/01/2022
#Tailai Wang


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        spots = k % n
        nums[:] = nums[(n - spots):] + nums[:(n - spots)]
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
