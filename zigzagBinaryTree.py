
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution(object):

    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        result=[]
        self.level(root,0,result)
        if len(result)!=0:
            for x in result:

                for i in range(len(x)-1):
                    x[i].next=x[i+1]
                x[-1].next=None





    def level(self,node,tree_level,result):
        if node is not None:
            if tree_level >= len(result):

                result.append([])

            result[tree_level].append(node)

            self.level(node.left,tree_level+1,result)
            self.level(node.right,tree_level+1,result)

















