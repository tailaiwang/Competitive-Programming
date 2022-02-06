#Removing Duplicates from an Unsorted Array
#Must be done in-place
#Inspired by https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/ (read it wrong lol)
#Tailai Wang

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        i = 0
        while i < k:
            cur = nums[i]
            count = 0
            j = i
            while j < k:
                tmp = nums[j]
                if tmp == cur:
                    count += 1
                    if count > 2:
                        nums.pop(j)
                        j -= 1
                        k -= 1
                j += 1
            i += 1
        return k
        
        
