class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        result=[]
        pdic=dict()
        for pchar in p:
            pdic[pchar]=pdic.get(pchar,0)+1

        sDic={}
        for schar in s[0:len(p)]:
            sDic[schar]=sDic.get(schar,0)+1

        if sDic==pdic:
            result.append(0)
        pLength=len(p)
        for i,schar in enumerate(s[len(p):]):
            sDic[schar]=sDic.get(schar,0)+1
            sDic[s[i]]=sDic[s[i]]-1
            sDic[s[i]]==0
            sDic.pop(s[i])
            if(sDic==pdic):
                result.append(i+1)

        return result



p={}
print p['test']


