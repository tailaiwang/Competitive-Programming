#Container With Most Water
#https://leetcode.com/problems/container-with-most-water/
#Mediun, 30/01/2022
#Tailai Wang

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        maxArea = min(height[l], height[r]) * (r -l)
        while (l < r):
            maxArea = max(maxArea, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return maxArea
    
