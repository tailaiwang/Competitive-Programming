#Majority Element
#https://leetcode.com/problems/majority-element/
#Easy (Data Structure II)
#Tailai Wang

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        output = None
        for num in nums:
            if count == 0:
                output = num
            if num == output:
                count += 1
            else:
                count -= 1
        return output
