#K Diff Pairs in An Array
#https://leetcode.com/problems/k-diff-pairs-in-an-array/
#Medium (Daily Challenge), 09/02/2022
#Tailai Wang

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = Counter(nums)
        retVal = 0
        if (k == 0):
            for item in nums:
                if nums[item] > 1:
                    retVal += 1
        else:
            for item in nums:
                if item - k in nums:
                    retVal += 1
        return retVal
