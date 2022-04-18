#Maximize Distance to Closest Person
#https://leetcode.com/problems/maximize-distance-to-closest-person/
#Medium (Daily Challenge), 15/01/2022
#Tailai Wang


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        ret = 1
        numEmpty = 0
        seen = False
        for seat in seats:
            if seat == 0:
                numEmpty += 1
                if (not seen):
                    ret = numEmpty
            if seat == 1:
                seen = True
                ret = max(ret, (numEmpty + 1)/ 2)
                numEmpty = 0
        return max(ret, numEmpty)
