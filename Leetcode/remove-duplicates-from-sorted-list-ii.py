<<<<<<< HEAD
#Remove Duplicates from Sorted List II
#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#Medium (Daily Challenge), 09/03/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = retval = ListNode(-101, head)
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                cur.next = head.next
            else:
                cur = cur.next
            head = head.next

            
            
        return retval.next
=======
#Remove Duplicates from Sorted List II
#https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
#Medium (Daily Challenge), 09/03/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = retval = ListNode(-101, head)
        while head:
            if head.next and head.next.val == head.val:
                while head.next and head.next.val == head.val:
                    head = head.next
                cur.next = head.next
            else:
                cur = cur.next
            head = head.next

            
            
        return retval.next
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
