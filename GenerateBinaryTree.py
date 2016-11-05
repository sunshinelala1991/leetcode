# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        r=self.generate2(1,n,{})
        return r





    def generate2(self,m,n,dic):

        if m==n:
            node=TreeNode(m)
            dic[str(m)+'-'+str(n)]=node
            return node

        if m>n:
            dic[str(m)+'-'+str(n)]=[]
            return []

        s=[]

        for i in range(m,n+1):
            tleft=[]
            if (str(m)+'-'+str(i-1)) in dic:
                tleft=dic[str(m)+'-'+str(i-1)]
            else:
                tleft=self.generate2(m,i-1,dic)

            tright=[]

            if (str(i+1)+'-'+str(n)) in dic:
                tright=dic[str(i+1)+'-'+str(n)]
            else:
                tright=self.generate2(i+1,n,dic)

            if len(tleft)!=0 and len(tright)!=0:
                for lt in tleft:
                    for rt in tright:
                        node=TreeNode(i)
                        node.left=lt
                        node.right=rt
                        s.append(node)

            elif len(tleft)!=0:
                for lt in tleft:
                    node=TreeNode(i)
                    node.left=lt
                    s.append(node)

            elif len(tright)!=0:
                for rt in tright:
                    node=TreeNode(i)
                    node.right=rt
                    s.append(node)

            else:
                node=TreeNode(i)
                s.append(node)


        dic[str(m)+'-'+str(n)]=s
        return s






