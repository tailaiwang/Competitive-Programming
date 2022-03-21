#Contains Duplicate
#https://leetcode.com/problems/contains-duplicate/
#Easy (Data Structures I), 20/03/2022
#Tailai Wang

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        checker = {}
        for num in nums:
            if num in checker:
                return True
            else:
                checker[num] = 1
        return False