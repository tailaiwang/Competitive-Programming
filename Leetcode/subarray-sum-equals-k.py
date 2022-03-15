<<<<<<< HEAD
#Subarray Sum Equals K
#https://leetcode.com/problems/subarray-sum-equals-k/
#Medium (Daily Challenge), 10/02/2022
#Tailai Wang

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        runningSum = 0
        table = collections.defaultdict(lambda:0)
        retVal = 0
        for x in nums:
            runningSum += x
            curSum = runningSum - k
            if curSum in table:
                retVal += table[curSum]
            if runningSum == k:
                retVal += 1
            table[runningSum] += 1
        return retVal
=======
#Subarray Sum Equals K
#https://leetcode.com/problems/subarray-sum-equals-k/
#Medium (Daily Challenge), 10/02/2022
#Tailai Wang

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        runningSum = 0
        table = collections.defaultdict(lambda:0)
        retVal = 0
        for x in nums:
            runningSum += x
            curSum = runningSum - k
            if curSum in table:
                retVal += table[curSum]
            if runningSum == k:
                retVal += 1
            table[runningSum] += 1
        return retVal
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
