#Maximum Subarray
#https://leetcode.com/problems/maximum-subarray/
#Easy, 13/02/2022
#Tailai Wang

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sums = []
        runningSum = 0
        for num in nums:
            runningSum += num
            sums.append(runningSum)
        
        low = sums[0]
        high = max(max(sums), max(nums))
        for i in sums:
            low = min(low, i)
            if (i != low):
                high = max(high, i - low)
        return high
