#Rotate List
#https://leetcode.com/problems/rotate-list/
#Medium (Daily Challenge), 11/03/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        last, n = head, 1
        while last.next:
            last = last.next
            n += 1
            
        if k % n == 0: return head
        
        middle = head
        for i in range(n - k%n-1):
            middle = middle.next
            
        new_head = middle.next
        last.next = head
        middle.next = None
        return new_head
