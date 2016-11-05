class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        return self.minimum(triangle,0,0,len(triangle),{})



    def minimum(self,triangle,i,j,tlen,dic):

        if i>=tlen:
            return 0

        if i==tlen-1:
            dic[str(i)+"-"+str(j)]=triangle[i][j]
            return triangle[i][j]

        leftmin=0
        rightmin=0

        if str(i+1)+"-"+str(j) in dic:
            leftmin=dic[str(i+1)+"-"+str(j)]
        else:
            leftmin=self.minimum(triangle,i+1,j,tlen)

        if str(i+1)+"-"+str(j+1) in dic:
            rightmin=dic[str(i+1)+"-"+str(j+1)]
        else:
            rightmin=self.minimum(triangle,i+1,j+1,tlen)

        dic[str(i)+"-"+str(j)]=triangle[i][j]+min(leftmin,rightmin)

        return triangle[i][j]+min(leftmin,rightmin)



