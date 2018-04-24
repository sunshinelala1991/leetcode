class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        base=0

        for i,a in enumerate(A):
            base+=i*a

        aLen=len(A)
        largest=base
        for i in range(len(A)-1,0,-1):
            newBase=base+sum(A)
            newBase-=aLen*A[i]
            if newBase>base:
                largest=newBase
            base= newBase
        return largest