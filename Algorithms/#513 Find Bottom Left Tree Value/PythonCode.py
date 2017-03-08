"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2: 
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val, height = self.recursiveSolution(root)
        
        return val
        
        
    def recursiveSolution(self, root):
        
        if root.left is not None:
            left_val, left_height = self.recursiveSolution(root.left)
        if root.right is not None:
            right_val, right_height = self.recursiveSolution(root.right)
            
        if root.left is None and root.right is None:
            return root.val, 0
        elif root.right is None:
            return left_val, left_height + 1
        elif root.left is None:
            return right_val, right_height + 1
        else:
            if left_height >= right_height:
                return left_val, left_height + 1
            else:
                return right_val, right_height + 1
        



