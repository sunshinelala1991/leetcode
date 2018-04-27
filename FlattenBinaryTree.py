
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        nodesList=[]

        self.inOrderDFS(root,nodesList)

        for i,n in enumerate(nodesList[:-1]):
            n.right=nodesList[i+1]
        return root





    def inOrderDFS(self, node, nodesList):

        if node==None:
            return
        else:
            nodesList.append(node)
            self.inOrderDFS(node.left, nodesList)
            self.inOrderDFS(node.right,nodesList)




