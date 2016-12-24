class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if self.balancedHelper(root) ==False:
            return False
        return True



    def balancedHelper(self,node):
        if node==None:
            return  0

        if node.left==None and node.right==None:
            return 1

        if node.left!=None and node.right==None:
            lh=self.balancedHelper(node.left)
            rh=0
            if lh==False:
                return False
            else:
                if lh-rh>1:
                    return False
                return lh+1

        if node.right!=None and node.left==None:
            lh=0
            rh=self.balancedHelper(node.right)
            if rh==False:
                return False
            else:
                if rh-lh>1:
                    return False
                return rh+1

        lh=self.balancedHelper(node.left)
        rh=self.balancedHelper(node.right)
        if lh==False or rh==False:
            return False
        else:
            if abs(lh-rh)>1:
                return False
            return max(lh,rh)+1