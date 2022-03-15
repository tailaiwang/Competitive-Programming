#Subsets
#https://leetcode.com/problems/subsets/
#Medium, 02/01/2022
#Tailai Wang

class Solution(object):
    megaoutput = []
    
    def subsetsHelper(self, nums, output, i):
        if i == len(nums):
            trueoutput = []
            for i in range (len(output)):
                if output[i] != 0:
                    trueoutput.append(nums[i])
            self.megaoutput.append(trueoutput)
        else:
            output[i] = 0
            self.subsetsHelper(nums, output, i+1)
            output[i] = 1
            self.subsetsHelper(nums, output, i+1)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.megaoutput = []
        output = [0 for i in range(len(nums))]
        self.subsetsHelper(nums, output, 0)
        return self.megaoutput
        
