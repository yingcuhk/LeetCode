# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        Queue = [root]
        
        LO = []
        while len(Queue)>0:
            NewQueue = []
            lo = []
            for node in Queue:
                lo.append(node.val)
                if node.left is not None:
                    NewQueue.append(node.left)
                if node.right is not None:
                    NewQueue.append(node.right)
            LO.append(lo)
            
            Queue = NewQueue
            
        return LO
                
                
                
                
                
                
                