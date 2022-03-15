#Jump Game II
#https://leetcode.com/problems/jump-game-ii/
#Medium, 27/01/2022
#Tailai Wang

class Solution(object):
    output = float('inf')
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times
