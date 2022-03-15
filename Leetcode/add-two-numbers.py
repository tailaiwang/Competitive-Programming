<<<<<<< HEAD
#Add Two Numbers
#https://leetcode.com/problems/add-two-numbers/
#Medium, 12/02/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = None
        curNode = None
        carry = 0
        while l1 or l2:
            l1val = l1.val if l1 != None else 0
            l2val = l2.val if l2 != None else 0
            cur = l1val + l2val + carry
            if cur > 9:
                cur = cur - 10
                carry = 1
            else:
                carry = 0
            if output == None:
                output = ListNode(cur)
                curNode = output
            else:
                curNode.next = ListNode(cur)
                curNode = curNode.next
            if l1 != None:
                l1 = l1.next
            if l2!= None:
                l2 = l2.next
        if (carry != 0):
            curNode.next = ListNode(1)
            
        return output
            
=======
#Add Two Numbers
#https://leetcode.com/problems/add-two-numbers/
#Medium, 12/02/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        output = None
        curNode = None
        carry = 0
        while l1 or l2:
            l1val = l1.val if l1 != None else 0
            l2val = l2.val if l2 != None else 0
            cur = l1val + l2val + carry
            if cur > 9:
                cur = cur - 10
                carry = 1
            else:
                carry = 0
            if output == None:
                output = ListNode(cur)
                curNode = output
            else:
                curNode.next = ListNode(cur)
                curNode = curNode.next
            if l1 != None:
                l1 = l1.next
            if l2!= None:
                l2 = l2.next
        if (carry != 0):
            curNode.next = ListNode(1)
            
        return output
            
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
