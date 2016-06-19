# Definition for a binary tree node.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        # non recursive solution 
        if len(preorder) == 0:
            return None
        rootval = preorder[0]
        Root = TreeNode(rootval)
        curnode = Root
        nodeStack = [Root]
        valStack = [rootval]
        for val in preorder[1:]:
            curnode = nodeStack[-1]
            curval = valStack[-1]
            newnode = TreeNode(val)
            if inorder.index(val) < inorder.index(curval):
                curnode.left = newnode
                nodeStack.append(newnode)
                valStack.append(val)
            else:
                while 1:
                    Flag = True
                    for tempval in inorder[inorder.index(curval)+1:inorder.index(val)]:
                        if tempval in valStack:
                            Flag = False
                            break
                    if not Flag:
                        nodeStack.pop()
                        valStack.pop()
                        curnode = nodeStack[-1]
                        curval = valStack[-1]
                    else:
                        curnode = nodeStack[-1]
                        curval = valStack[-1]
                curnode.right = newnode
                nodeStack.append(newnode)
                valStack.append(val)
        return Root   
        
        
        """
        # a reucrsive soltuion using another function to save memory
        # return self.recursive(preorder,inorder,0,len(preorder)-1,0,len(inorder)-1)
        """
        
        
        """
        # another recursive solution but exceeding memory limit 
        if len(preorder) == 0:
            return None
        
        rootval = preorder[0]
        Root = TreeNode(rootval) # the left and right children are initialized as None
        # to find the root position
        L = inorder.index(rootval)
        
        # leftTree_inorder = inorder[:L]
        # rightTree_inorder = inorder[L+1:]
        # leftTree_preorder = preorder[1:L+1]
        # rightTree_preorder = preorder[L+1:]
        
        # leftTree = self.buildTree(leftTree_preorder,leftTree_inorder)
        # rightTree = self.buildTree(rightTree_preorder,rightTree_inorder)
        
        
        leftTree = self.buildTree(preorder[1:L+1],inorder[:L])
        rightTree = self.buildTree(preorder[L+1:],inorder[L+1:])
        Root.left = leftTree
        Root.right = rightTree
        
        return Root
        """
    def recursive(self,preorder,inorder,prefirst,prelast,infirst,inlast):
        
        if prefirst > prelast:
            return None
        rootval = preorder[prefirst]
        newnode = TreeNode(rootval)
        
        root_pos_in = inorder.index(rootval)
        
        # left tree
        infirst_left = infirst
        inlast_left =  root_pos_in-1
        
        prefirst_left = prefirst + 1
        prelast_left = prefirst_left+inlast_left-infirst_left
        # right tree
        
        infirst_right = root_pos_in+1
        inlast_right = inlast
        
        prelast_right = prelast
        prefirst_right = prelast - (inlast_right-infirst_right)
        
        
        newnode.left = self.recursive(preorder,inorder,prefirst_left,prelast_left,infirst_left,inlast_left)
        newnode.right = self.recursive(preorder,inorder,prefirst_right,prelast_right,infirst_right,inlast_right)
        
        return newnode
        
       