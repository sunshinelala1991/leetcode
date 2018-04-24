class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        sDic={}
        for i, schar in enumerate(S):
            if schar not in sDic:
                sDic[schar]=[]
            sDic[schar].append(i)

        print sDic
        result=0

        for word in words:
            previous=-1
            wflag=True
            for w in word:
                flag=False
                if w in sDic:
                    for p in sDic[w]:
                        if p>previous:
                            previous=p
                            flag=True
                            break
                if not flag:
                    wflag=False
                    break
            if wflag:
                result+=1



        return result


s= Solution()
print s.numMatchingSubseq("abcde",["a", "bb", "acd", "ace"])
