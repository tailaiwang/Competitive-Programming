#Validate Stack Sequences
#https://leetcode.com/problems/validate-stack-sequences/
#Medium (Daily Challenge), 15/03/2022
#Tailai Wang

class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        n = 0
        for x in pushed:
            stack.append(x)
            while stack and n < len(popped) and stack[-1] == popped[n]:
                stack.pop()
                n += 1
        return n == len(popped)