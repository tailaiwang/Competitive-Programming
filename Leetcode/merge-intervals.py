#Merge Intervals
#https://leetcode.com/problems/merge-intervals/
#Medium (Data Structures II), 18/04/2022
#Tailai Wang

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        retval = []
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        
        for interval in intervals:
            if interval[0] > end:
                retval.append([start, end])
                start = interval[0]
                end = interval[1]
            else:
                end = max(interval[1], end)
        retval.append([start, end])
        return retval
                