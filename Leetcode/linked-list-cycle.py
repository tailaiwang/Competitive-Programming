#Linked List Cycle
#https://leetcode.com/problems/linked-list-cycle/
#Easy, 19/01/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        if head == None:
            return False
        while True:
            if slow.next == None:
                return False
            else:
                if fast.next != None:
                    fast = fast.next
                    if fast.next != None:
                        fast = fast.next
                if slow == fast:
                    return True
            slow = slow.next
