class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """

        cdic={}
        for c in s:
            cdic[c]=cdic.get(c,0)+1


        countdic={}
        cs=['z','w','u','x','o','r','f','s','g','n']
        digits=['zero','two','four','six','one','three','five','seven','eight','nine'];
        for c,d in zip(cs,digits)[0:4]:

            countdic[d]=cdic.get(c)

            if countdic[d]!=None and countdic[d]!=0:
                for x in d:
                    cdic[x]=cdic[x]-countdic[d]

        for c,d in zip(cs,digits)[4:8]:

            countdic[d]=cdic.get(c)
            if countdic[d]!=None and countdic[d]!=0 :
                for x in d:
                    cdic[x]=cdic[x]-countdic[d]

        for c,d in zip(cs,digits)[8:10]:

            countdic[d]=cdic.get(c)

            if c=='n':
                countdic[d]/=2

            if countdic[d]!=None and countdic[d]!=0:
                for x in d:
                    cdic[x]=cdic[x]-countdic[d]

        orderDigits=['zero',"one",'two','three','four','five','six','seven','eight','nine']

        result=''

        for d in orderDigits:
            if countdic[d]!=None and countdic[d]!=0:
                for i in range(countdic[d]):
                    result=result+str(orderDigits.index(d))

        return result






s=Solution();
print s.originalDigits("nnei")