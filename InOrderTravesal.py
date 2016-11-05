class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result=[]
        self.level(root,0,result)
        return result






    def level(self,node,tree_level,result):
        if node is not None:
            if tree_level >= len(result):

                result.append([])

            result[tree_level].append(node.val)

            self.level(node.left,tree_level+1,result)
            self.level(node.right,tree_level+1,result)



