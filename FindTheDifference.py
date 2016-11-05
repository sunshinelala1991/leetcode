class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """

        if len(pattern)!=len(str.split()):
            return False


        dic={}
        dic2={}
        for c,s in zip(pattern,str.split()):
            if c not in dic:
                dic[c]=s

            else:
                if dic[c]!=s:
                    return False

            if s not in dic2:
                dic2[s]=c

            else:
                if dic[s]!=c:
                    return False

        return True

























