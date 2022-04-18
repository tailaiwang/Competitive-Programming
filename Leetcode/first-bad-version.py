#First Bad Version
#https://leetcode.com/problems/first-bad-version/
#Easy (Algorithms I), 18/04/2022
#Tailai Wang


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 0
        r = n
        while (l <= r):
            mid = (l + r) // 2
            if (isBadVersion(mid)):
                r = mid - 1
            else:
                l = mid + 1
        return l