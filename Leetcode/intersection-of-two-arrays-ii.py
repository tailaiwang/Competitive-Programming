#Intersection of Two Arrays II
#https://leetcode.com/problems/intersection-of-two-arrays-ii/
#Easy (Data Structures I), 22/03/2022
#Tailai Wang

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c = Counter(nums1)
        output = []
        for num in nums2:
            if c[num] > 0:
                output.append(num)
                c[num] -= 1
        return output