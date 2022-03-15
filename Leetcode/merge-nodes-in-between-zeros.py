<<<<<<< HEAD
#Merge Nodes in Between Zeros
#https://leetcode.com/problems/merge-nodes-in-between-zeros/
#Medium, 05/03/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = spot = ListNode(0)
        head = head.next
        curSum = 0
        while head:
            if head.val == 0:
                tmp = ListNode(curSum)
                spot.next = tmp
                spot = spot.next
                curSum = 0
            else:
                curSum += head.val
            head = head.next
        return ret.next
    
=======
#Merge Nodes in Between Zeros
#https://leetcode.com/problems/merge-nodes-in-between-zeros/
#Medium, 05/03/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ret = spot = ListNode(0)
        head = head.next
        curSum = 0
        while head:
            if head.val == 0:
                tmp = ListNode(curSum)
                spot.next = tmp
                spot = spot.next
                curSum = 0
            else:
                curSum += head.val
            head = head.next
        return ret.next
    
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
