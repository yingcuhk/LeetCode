# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    """
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Flag = True
        fast = head
        slow = head
        while(1):
            if fast is None:
                return None
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            slow = slow.next
                
            if fast == slow:
                break
        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast

        