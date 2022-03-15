<<<<<<< HEAD
#Swap Nodes in Pairs
#https://leetcode.com/problems/swap-nodes-in-pairs/
#Medium, 08/02/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head
=======
#Swap Nodes in Pairs
#https://leetcode.com/problems/swap-nodes-in-pairs/
#Medium, 08/02/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
