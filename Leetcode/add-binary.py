#Add Binary
#https://leetcode.com/problems/add-binary/
#Easy (Daily Challenge), 09/01/2022
#Tailai Wang

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        output = ""
        cur = 0
        for i in range(1, min(len(a), len(b)) + 1):
            curA = a[len(a) - i]
            curB = b[len(b) - i]
            if cur == 0:
                if curA == "1" and curB == "0":
                    output = "1" + output
                elif curA == "0" and curB == "1":
                    output = "1" + output
                elif curA == "0" and curB == "0":
                    output = "0" + output
                else:
                    output = "0" + output
                    cur = 1
            else:
                if curA == "0" and curB == "0":
                    output = "1" + output
                    cur = 0
                elif curA == "1" and curB == "1":
                    output ="1" + output
                else:
                    output = "0" + output

        for i in range(min(len(a), len(b)) + 1, max(len(a), len(b)) + 1):
            if (len(a) > len(b)):
                if cur == 1:
                    if a[len(a) - i] == "1":
                        output = "0" + output
                    else:
                        output = "1" + output
                        cur = 0
                else:
                    if a[len(a) - i] == "1":
                        output = "1" + output
                    else:
                        output = "0" + output
            else:
                if cur == 1:
                    if b[len(b) - i] == "1":
                        output = "0" + output
                    else:
                        output = "1" + output
                        cur = 0
                else:
                    if b[len(b) - i] == "1":
                        output = "1" + output
                    else:
                        output = "0" + output

        if (cur == 1):
            output = "1" + output
        return output
