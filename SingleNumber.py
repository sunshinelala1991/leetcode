import itertools

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s)==0:
            return []
        if len(s)==1:
            return [[s]]

        k=self.part(s,{})
        k.sort()
        return list(k for k,_ in itertools.groupby(k))





    def part(self,s,dic):
        if len(s)==1:
            dic[s]=[[s]]
            return [[s]]

        else:
            if s in dic:
                return dic[s]

            result=[]
            for i in range(1,len(s)):
                left=0
                if s[0:i] in dic:
                    left=dic[s[0:i]]
                else:
                    left=self.part(s[0:i],dic)

                right=0
                if s[i:] in dic:
                    right=dic[s[i:]]
                else:
                    right=self.part(s[i:],dic)

                for x in left:
                    for y in right:
                        result.append(x+y)

            if s==s[::-1]:
                result.append([s])

            dic[s]=result
            return result










