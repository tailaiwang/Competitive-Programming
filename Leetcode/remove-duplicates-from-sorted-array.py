<<<<<<< HEAD
#Remove Duplicates from Sorted Array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#Easy, 18/02/2022
#Tailai Wang


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        prev = nums[0]
        while True:
            if i >= len(nums):
                return len(nums)
            cur = nums[i]
            if (cur == prev):
                del nums[i]
            else:
                i += 1
            prev = cur

        
=======
#Remove Duplicates from Sorted Array
#https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#Easy, 18/02/2022
#Tailai Wang


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        prev = nums[0]
        while True:
            if i >= len(nums):
                return len(nums)
            cur = nums[i]
            if (cur == prev):
                del nums[i]
            else:
                i += 1
            prev = cur

        
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
