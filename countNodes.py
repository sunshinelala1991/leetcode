# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        leftd=self.leftDepth(root)
        rightd=self.rightDepth(root)

        if leftd==rightd:
            return 2**leftd-1

        else:
            return self.countNodes(root.left)+self.countNodes(root.right)+1




    def leftDepth(self,root):

        count=0

        while root is not None:
            count+=1
            root=root.left

        return count

    def rightDepth(self,root):

        count=0

        while root is not None:
            count+=1
            root=root.right

        return count
