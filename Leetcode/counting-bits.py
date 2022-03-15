<<<<<<< HEAD
#Counting Bits
#https://leetcode.com/problems/counting-bits/
#Easy (Daily Challenge), 01/03/2022
#Tailai Wang

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [0]
        for i in range(1, n + 1):
            output.append(output[i >> 1] + i % 2)
        return output
=======
#Counting Bits
#https://leetcode.com/problems/counting-bits/
#Easy (Daily Challenge), 01/03/2022
#Tailai Wang

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        output = [0]
        for i in range(1, n + 1):
            output.append(output[i >> 1] + i % 2)
        return output
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
