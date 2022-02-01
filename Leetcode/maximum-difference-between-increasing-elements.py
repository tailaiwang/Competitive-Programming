class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxDistance = -1
        minNumber = float('inf')
        prev = nums[0]
        for i in range(len(nums)):
            cur = nums[i]
            minNumber = min(minNumber, cur)
            if (cur > prev):
                maxDistance = max(maxDistance, cur - minNumber)
            prev = cur
        return maxDistance
