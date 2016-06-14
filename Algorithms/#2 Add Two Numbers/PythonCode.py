"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""

# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        SumResult = ListNode(0)
        curnode = SumResult
        cur1 = l1
        cur2 = l2
        add1 = 0
        while cur1 is not None or cur2 is not None or add1 > 0:
            if cur1 is None:
                val1 = 0
            else:
                val1 = cur1.val
            if cur2 is None:
                val2=  0
            else:
                val2 = cur2.val
            digsum = val1 + val2 + add1
            add1 = digsum / 10
            digsum = digsum % 10
            newnode = ListNode(digsum)
            if cur1 is not None:
                cur1 = cur1.next
            if cur2 is not None:
                cur2 = cur2.next
            curnode.next = newnode
            curnode = newnode
            
        return SumResult.next
        
        """
        SumResult = ListNode(0)
        curnode = SumResult
        cur1 = l1
        cur2 = l2
        add1 = 0
        while cur1 is not None or cur2 is not None or add1 > 0:
            if cur1 is None and cur2 is not None:

                digsum = cur2.val + add1
                add1 = digsum / 10
                digsum = digsum % 10
                newnode = ListNode(digsum)
                cur2 = cur2.next
                curnode.next = newnode
                curnode = newnode
                continue
            if cur1 is not None and cur2 is None:
                digsum = cur1.val + add1
                add1 = digsum / 10
                digsum = digsum % 10
                newnode = ListNode(digsum)
                #newnode.val = digsum
                cur1 = cur1.next
                curnode.next = newnode
                curnode = newnode
                continue
            
            if cur1 is not None and cur2 is not None:
                digsum = cur1.val + cur2.val + add1
                add1 = digsum / 10
                digsum = digsum % 10
                newnode = ListNode(digsum)
                #newnode.val = digsum
                cur1 = cur1.next
                cur2 = cur2.next
                curnode.next = newnode
                curnode = newnode
                continue
            if cur1 is None and cur2 is None:
                digsum = add1
                add1 = digsum / 10
                digsum = digsum % 10
                newnode = ListNode(digsum)
                #newnode.val = digsum
                curnode.next = newnode
                curnode = newnode

            
        
        return SumResult.next
        """