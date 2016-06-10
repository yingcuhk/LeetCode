"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 ¡ú a2
                   ¨K
                     c1 ¡ú c2 ¡ú c3
                   ¨J            
B:     b1 ¡ú b2 ¡ú b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        heada = headA
        headb = headB
        diff = 0
        while heada is not None and headb is not None:
            heada = heada.next
            headb = headb.next
        if heada == None:
            head = headb
            head1 = headB
            head2 = headA
        else:
            head = heada
            head1 = headA
            head2 = headB
            
        while head is not None:
            head = head.next
            diff += 1
        
        """
        LA = 0
        LB = 0
        while heada is not None:
            LA += 1
            heada = heada.next
        while headb is not None:
            LB += 1
            headb = headb.next
        diff = abs(LA-LB)
        """
        """
        if LA > LB:
            head1 = headA
            head2 = headB
        else:
            head1 = headB
            head2 = headA
        """
        
        for k in xrange(diff):
            head1 = head1.next
        
        while head1 is not None:
            if head1.val == head2.val:
                break
            head1 = head1.next
            head2 = head2.next
            
        return head1
            

            