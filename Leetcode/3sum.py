#3 Sum
#https://leetcode.com/problems/3sum
#Medium (Algorithms II), 20/03/2022
#Tailai Wang

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                if (nums[l] + nums[r] + nums[i] > 0):
                    r -= 1
                elif (nums[l] + nuz`ms[r] + nums[i] < 0):
                    l += 1
                else:
                    ret.append([nums[l], nums[r], nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
               
        return ret
                