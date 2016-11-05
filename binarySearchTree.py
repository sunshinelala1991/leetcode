class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.num(n,{})

    def num(self,n,dic):
        if n==0:
            dic['0']=1
            return 1
        if n==1:
            dic['1']=1
            return 1
        if n==2:
            dic['2']=2
            return 2

        s=0
        left=0
        right=0
        for i in range(n):
            if str(i) in dic:
                left=dic[str(i)]
            else:
                left=self.num(i)

            if str(n-1-i) in dic:
                right=dic[str(n-1-i)]
            else:
                right=self.num(n-1-i)
            s+=left*right

        dic[str(n)]=s
        return s
