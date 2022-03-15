<<<<<<< HEAD
#Linked List Cycle II
#https://leetcode.com/problems/linked-list-cycle-ii/
#Medium (Daily Challenge), 19/01/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        found =[]
        slow = head
        fast = head
        if head == None:
            return None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found.append(slow)
                while True:
                    slow = slow.next
                    if (slow == fast):
                        break
                    else:
                        found.append(slow)
                slow = head
                while True:
                    if (slow in found):
                        return slow
                    slow = slow.next
        return None
=======
#Linked List Cycle II
#https://leetcode.com/problems/linked-list-cycle-ii/
#Medium (Daily Challenge), 19/01/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        found =[]
        slow = head
        fast = head
        if head == None:
            return None
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                found.append(slow)
                while True:
                    slow = slow.next
                    if (slow == fast):
                        break
                    else:
                        found.append(slow)
                slow = head
                while True:
                    if (slow in found):
                        return slow
                    slow = slow.next
        return None
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
