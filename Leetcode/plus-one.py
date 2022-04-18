#Plus One
#https://leetcode.com/problems/plus-one/submissions/
#Easy, 17/02/2022
#Tailai Wang

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        if digits[n - 1] != 9:
            digits[n-1] += 1
            return digits
        else:
            carry = 0
            for i in range (n - 1, -1, -1):
                if digits[i] == 9:
                    digits[i] = 0
                    carry = 1
                else:
                    digits[i] += 1
                    carry = 0
                    break
            if carry == 1:
                digits.insert(0, 1)
        return digits
