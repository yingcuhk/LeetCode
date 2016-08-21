# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        # Non-recursive solution
        
        prelist = [root.val]
        nodeStack = [root]
        visitTime = [1]
        
        
        while nodeStack:
            #print visitTime
            node = nodeStack[-1]
            if visitTime[-1] == 1:
                if node.left is not None:
                    prelist.append(node.left.val)
                    nodeStack.append(node.left)
                    visitTime.append(1)
                else:
                    visitTime[-1] += 1
            elif visitTime[-1] == 2:
                if node.right is not None:
                    prelist.append(node.right.val)
                    nodeStack.append(node.right)
                    visitTime.append(1)
                else:
                    visitTime[-1] += 1
            else:
                nodeStack.pop()
                visitTime.pop()
                if visitTime:
                    visitTime[-1] += 1
            
        return prelist
        
        """
        # recursive solution 
        return self.preorderRecursive(root)
        
    def preorderRecursive(self, node):
        
        
        prelist = [node.val]
        
        if node.left is not None:
            prelist += self.preorderRecursive(node.left)
        if node.right is not None:
            prelist += self.preorderRecursive(node.right)
            
        return prelist
        """
        """
        if node.left is None:
            leftstr = []
        else:
            leftstr = self.preorderRecursive(node.left)
            
        if node.right is None:
            rightstr = []
        else:
            rightstr = self.preorderRecursive(node.right)
        
        midstr = [node.val]
        
        return midstr + leftstr + rightstr
        """
            

            
            
            
        