# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:
     3
    / \
   2   3
    \   \ 
     3   1
Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:
     3
    / \
   4   5
  / \   \ 
 1   3   1
Maximum amount of money the thief can rob = 4 + 5 = 9.
"""
def reducerob(root):
        if root == None:
            return 0, 0 # value select root, value not select root
            
        val0_left, val1_left = reducerob(root.left)
        val0_right, val1_right = reducerob(root.right)
        
        val_left = root.val + val1_left + val1_right
        val_right = max(val0_left,val1_left) + max(val0_right,val1_right)
        
        return val_left, val_right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        val1,val2 = reducerob(root)
        
        return max(val1,val2)
            
    
            