# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        lis=self.inorder(root)

        if len(lis)<=1:
            return True

        p=lis[0]

        for q in lis[1:]:
            if q<p:
                return False
            p=q



    def inorder(self,node):
        if node==None:
            return []
        if node.left==None and node.right==None:
            return [node.val]

        else:
            l=self.inorder(node.left)
            r=self.inorder(node.right)
            return l+[node.val]+r