class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        nl=[]

        self.inOrder(root,nl)

        flag=True
        for i in range(len(nl)-1):
            if nl[i]>=nl[i+1]:
                flag=False

        return flag




    def isValid(self,node):

        if node ==None:
            return True

        elif node.left==None and node.right != None:

            return node.val<node.right.val and self.isValid(node.right)

        elif node.left!=None and node.right==None:
            return node.val>node.left.val and self.isValid(node.left)

        elif node.left==None and node.right==None:
            return True
        else:
            return node.val<node.right.val and self.isValid(node.right) and node.val>node.left.val and self.isValid(node.left)


    def inOrder(self,node,nl):

        if node==None:
            return

        elif node.left==None and node.right==None:
            nl.append(node.val)

        elif node.left!=None and node.right==None:
            self.inOrder(node.left,nl)
            nl.append(node.val)
        elif node.left==None and node.right != None:
            nl.append(node.val)
            self.inOrder(node.right,nl)
        else:
            self.inOrder(node.left,nl)
            nl.append(node.val)
            self.inOrder(node.right,nl)
