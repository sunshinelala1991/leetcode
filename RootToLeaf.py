# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root==None:
            return 0
        resultList=self.sum(root)

        result=0
        for x in resultList:
            result=result+int(x)

        return result



    def sum(self,node):
        if node.left==None and node.right==None:
            return [str(node.val)]

        elif node.right!=None and node.left==None:
            rightSum=self.sum(node.right)

            for i in range(len(rightSum)):
                rightSum[i]=str(node.val)+rightSum[i]

            return rightSum
        elif node.left!=None and node.right==None:
            leftSum=self.sum(node.left)

            for i in range(len(leftSum)):
                leftSum[i]=str(node.val)+leftSum[i]

            return leftSum

        else:

            rightSum=self.sum(node.right)

            for i in range(len(rightSum)):
                rightSum[i]=str(node.val)+rightSum[i]

            leftSum=self.sum(node.left)

            for i in range(len(leftSum)):
                leftSum[i]=str(node.val)+leftSum[i]


            return leftSum+rightSum



