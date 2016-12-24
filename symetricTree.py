class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root==None:
            return True
        return self.symmetricHelper(root.left,root.right)

    def symmetricHelper(self,nodea,nodeb):
        if nodea==None:
            if nodeb!=None:
                return False
            else:
                return True

        if nodeb==None:
            return False
        if nodea.val!=nodeb.val:
            return False

        return self.symmetricHelper(nodea.left,nodeb.right) and self.symmetricHelper(nodea.right,nodeb.left)