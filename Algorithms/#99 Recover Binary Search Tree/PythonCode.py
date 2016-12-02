# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

"""
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        
        
        leftmis = self.leftMisNode(root)
        rightmis = self.rightMisNode(root)
        
        temp = leftmis.val
        leftmis.val = rightmis.val
        rightmis.val = temp
        
        
    def leftMisNode(self,root):
        
        Stack = [root]
        Status = []
        Visited = [False]
        
        last_val = -1*float('inf')
        last_node = None
        count = 1
        while Stack:
            if Stack[-1].left and not Visited[-1]:
                Stack.append(Stack[-1].left)
                Visited[-1] = True
                Visited.append(False)
            else:
                node = Stack.pop()
                Visited.pop()
                val = node.val
                if val >= last_val:
                    last_val = val
                    last_node = node
                else:
                    return last_node
                    
                if node.right:
                    Stack.append(node.right)
                    Visited.append(False)

        return None
        
    def rightMisNode(self,root):
    
    
        Stack = [root]
        Visited = [False]
        
        last_val = float('inf')
        last_node = None
        while Stack:
            if Stack[-1].right is not None and not Visited[-1]:
                Stack.append(Stack[-1].right)
                Visited[-1] = True
                Visited.append(False)
            else:
                node = Stack.pop()
                Visited.pop()
                val = node.val
                if val <= last_val:
                    last_val = val
                    last_node = node
                else:
                    return last_node
                    
                if node.left is not None:
                    Stack.append(node.left)
                    Visited.append(False)
        return None 
                    