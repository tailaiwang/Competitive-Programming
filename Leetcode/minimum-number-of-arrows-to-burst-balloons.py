#Minimum Number of Arrows to Burst Balloons
#https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
#Medium (Daily Challenge), 13/01/2022
#Tailai Wang


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda x: (x[1]))
        arrows = 0
        curLast = -float('inf')
        for point in points:
            if point[0] > curLast:
                arrows += 1
                curLast = point[1]
        return arrows
