class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        dic={}
        return self.decode(s,0,dic)


    def decode(self,s,i,dic):
        if i==len(s)-1 and s[i]!="0":
            return 1

        if i==len(s):
            return 1

        if s[i]=='0':
            return 0

        if int(s[i:i+2])<=26:
            if int(s[i:i+2]) ==10 or int(s[i:i+2])==20:
                if s[i+2:] in dic:
                    dic[s[i:]]=dic[s[i+2:]]
                else:

                    dic[s[i:]]=self.decode(s,i+2,dic)

                return dic[s[i:]]
            else:
                p=0
                if s[i+1:] in dic:
                    p=dic[s[i+1:]]
                else:
                    p=self.decode(s,i+1,dic)
                q=0
                if s[i+2:] in dic:
                    q=dic[s[i+2:]]
                else:
                    q=self.decode(s,i+2,dic)



                dic[s[i:]]=p+q

                return dic[s[i:]]
        else:
            if s[i+1:] in dic:
                dic[s[i:]]=dic[s[i+1:]]
            else:
                dic[s[i:]]=self.decode(s,i+1,dic)
            return dic[s[i:]]
