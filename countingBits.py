class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if len(A)<3:
            return 0

        slen=[]

        j=2
        dis=A[1]-A[0]
        sl=2
        for i in range(1,len(A)-1):
            if A[j]-A[i]==dis:
                sl+=1
                if j==len(A)-1:
                    slen.append(sl)

            else:
                slen.append(sl)
                dis=A[j]-A[i]
                sl=2



            j+=1
        sum=0
        for sl in slen:
            if sl>2:
                sum=sum+(sl-2+1)*(sl-2)/2

        return sum






