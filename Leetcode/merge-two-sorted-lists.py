<<<<<<< HEAD
#Merge Two Sorted Lists
#https://leetcode.com/problems/merge-two-sorted-lists/
#Easy, 15/01/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val < list2.val:
                ret = ListNode(list1.val, None)
                list1 = list1.next
                ptr = ret
            else:
                ret = ListNode(list2.val, None)
                list2 = list2.next
                ptr = ret
            while True:
                if list1 == None:
                    ptr.next = list2
                    break
                elif list2 == None:
                    ptr.next = list1
                    break
                else:
                    if list1.val < list2.val:
                        newNode = ListNode(list1.val, None)
                        ptr.next = newNode
                        ptr = ptr.next
                        list1 = list1.next
                    else:
                        newNode = ListNode(list2.val, None)
                        ptr.next = newNode
                        ptr = ptr.next
                        list2 = list2.next
            return ret
                
=======
#Merge Two Sorted Lists
#https://leetcode.com/problems/merge-two-sorted-lists/
#Easy, 15/01/2022
#Tailai Wang

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            if list1.val < list2.val:
                ret = ListNode(list1.val, None)
                list1 = list1.next
                ptr = ret
            else:
                ret = ListNode(list2.val, None)
                list2 = list2.next
                ptr = ret
            while True:
                if list1 == None:
                    ptr.next = list2
                    break
                elif list2 == None:
                    ptr.next = list1
                    break
                else:
                    if list1.val < list2.val:
                        newNode = ListNode(list1.val, None)
                        ptr.next = newNode
                        ptr = ptr.next
                        list1 = list1.next
                    else:
                        newNode = ListNode(list2.val, None)
                        ptr.next = newNode
                        ptr = ptr.next
                        list2 = list2.next
            return ret
                
>>>>>>> ba49908b5b4d7d2990ceb0c0f59ad013ea443c99
