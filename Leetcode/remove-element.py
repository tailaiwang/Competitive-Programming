#Remove Element
#https://leetcode.com/problems/remove-element/
#Easy, 23/02/2022
#Tailai Wang

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while nums.count(val) != 0:
            nums.remove(val)
