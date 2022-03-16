#Queries on Number of Points Inside a Circle
#https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
#Medium, 16/03/2022
#Tailai Wang

import math
class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        for query in queries:
            cur = 0
            x0 = query[0]
            y0 = query[1]
            r = query[2]
            for point in points:
                if math.sqrt((point[0] - x0) ** 2 + (point[1] - y0)**2) <=  r:
                    cur += 1
            answer.append(cur)
        return answer
                    