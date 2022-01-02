#Permutations
#https://leetcode.com/problems/permutations/
#Medium, 01/01/2022
#Tailai Wang

class Solution(object):
    def permute(self, nums):
        retval = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            top = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                retval.append([top] + perm)
            nums.append(top)
        return retval
        
