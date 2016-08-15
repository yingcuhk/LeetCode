"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        cur = head
        
        if cur is None:
            return None
        L = 1 # list length
        while cur.next is not None: # compute the length and find the tail
            L += 1
            cur = cur.next
        tail = cur
        if L == 0:
            return head 
        if k >= L:
            k = k % L
        
        P = L-k
        
        if P == L:
            return head
        cur = head
        for x in xrange(P-1):
            cur = cur.next
        
        newtail = cur
        newhead = cur.next

        tail.next = head
        newtail.next = None
        
        return newhead