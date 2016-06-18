# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        fakehead = ListNode(-1)
        fakehead.next = head
        
        pre = head 
        cur = pre.next
        while cur is not None:

            if cur.val < pre.val:
                pre.next = cur.next
                tempcur = fakehead
                
                while tempcur.next.val < cur.val:
                    tempcur = tempcur.next
                    
                    
                # insert the node
                tempnext = tempcur.next
                tempcur.next = cur
                cur.next = tempnext
                
                cur = pre.next
            else:
                pre = pre.next
                cur = cur.next
            
        return fakehead.next
        