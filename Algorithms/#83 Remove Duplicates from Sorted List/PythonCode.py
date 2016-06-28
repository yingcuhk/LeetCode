# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head is None or head.next is None:
            return head
            
        cur = head
        
        while cur is not None and cur.next is not None:
            
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return head 