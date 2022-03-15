<<<<<<< HEAD
#Remove Duplicated from Sorted Array II
#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#Medium (Daily Challenge), 06/02/2022
#Tailai Wang

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        k = len(nums)
        while i + 2 < k:
            if (nums[i] == nums[i + 2]):
                nums.pop(i+2)
                i -= 1
                k -= 1
            i += 1
        return k
        
        
        
        
=======
#Remove Duplicated from Sorted Array II
#https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
#Medium (Daily Challenge), 06/02/2022
#Tailai Wang

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        k = len(nums)
        while i + 2 < k:
            if (nums[i] == nums[i + 2]):
                nums.pop(i+2)
                i -= 1
                k -= 1
            i += 1
        return k
        
        
        
        
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
