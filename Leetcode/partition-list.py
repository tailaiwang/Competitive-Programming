<<<<<<< HEAD
#Partition List
#https://leetcode.com/problems/partition-list/
#Medium, 04/03/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = afterHead.next
        return beforeHead.next
                    
=======
#Partition List
#https://leetcode.com/problems/partition-list/
#Medium, 04/03/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        before = beforeHead = ListNode(0)
        after = afterHead = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = afterHead.next
        return beforeHead.next
                    
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
