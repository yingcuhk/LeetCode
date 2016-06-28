# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        fakehead = ListNode(0)
        fakehead.next = head
        
        cur = head
        prenode = fakehead
        while cur is not None and cur.next is not None:
            if cur.val == cur.next.val:
                tempval = cur.val
                while cur is not None and cur.val == tempval:
                    cur = cur.next
                prenode.next = cur
            else:
                prenode = cur 
                cur = cur.next
                
        return fakehead.next
        