#Merge K Sorted Lists
#https://leetcode.com/problems/merge-k-sorted-lists/
#Hard, 08/03/2022
#Tailai Wang

from Queue import PriorityQueue

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = spot = ListNode(0)
        pq = PriorityQueue()
        for l in lists:
            if l:
                #insert into priority queue
                pq.put((l.val, l))
        while pq.empty() == False:
            val, cur = pq.get()
            spot.next = ListNode(val)
            spot = spot.next
            cur = cur.next
            if cur:
                pq.put((cur.val, cur))
        return head.next
