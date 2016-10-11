"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
            
        F, temp = self.DepthofTree(root)
        
        return F
            
        
    def DepthofTree(self, root):
        if root is None:
            return True, 0
        F1, leftD = self.DepthofTree(root.left)
        F2, rightD = self.DepthofTree(root.right)
        
        #if not (F1 and F2):
        #    return False, 0
        Depth = 1 + max(leftD, rightD)
        
        Flag = leftD-rightD <= 1 and leftD-rightD >= -1
        
        Flag = Flag and F1 and F2

        return Flag, Depth