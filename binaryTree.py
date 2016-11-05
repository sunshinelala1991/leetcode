# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root==None:
            return []
        rl=[]
        self.inorder(root,rl)
        return rl

    def inorder(self,node,rl):

        if node.left==None and node.right==None:
            rl.append(node.val)

        elif node.left!=None and node.right==None:
            self.inorder(node.left,rl)
            rl.append(node.val)
        elif node.right!=None and node.left==None:
            rl.append(node.val)
            self.inorder(node.right,rl)
        else:
            self.inorder(node.left,rl)
            rl.append(node.val)
            self.inorder(node.right,rl)
