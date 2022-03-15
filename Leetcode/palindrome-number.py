class Solution(object):
    def isPalindrome(self, x):
        if (x < 0):
            return (False)
        inputVal = x
        new = 0
        while (inputVal > 0):
            new = new * 10 + inputVal % 10
            inputVal = inputVal // 10
        return ( new == x)



