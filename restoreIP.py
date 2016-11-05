class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<4:
            return []

        if len(s)>12:
            return []

        return self.ip(s,0,4)



    def ip(self,s,i,n):


        if i==len(s)-3:
            if n==3:
                return [s[-3]+'.'+s[-2]+'.'+s[-1]]
            elif n==2:
                if s[-3]!='0' and s[-2]!='0':
                    return [s[-3:-1]+'.'+s[-1],s[-3]+'.'+s[-2:]]
                elif s[-3]!='0':
                    return [s[-3:-1]+'.'+s[-1]]
                elif s[-2]!='0':
                    return [s[-3]+'.'+s[-2:]]
                else:
                    return None
            elif n==1:
                if s[-3]!='0' and int(s[-3:])<256:
                    return[s[-3:]]
                else:
                    return None
            else:
                return None


        if i==len(s)-2:
            if n==2:
                return [s[-2]+'.'+s[-1]]
            if n==1:
                if s[-2]!='0':
                    return [s[-2:]]
                else:
                    return None
            else:
                return None

        if i==len(s)-1:
            if n==1:
                return [s[-1]]
            else:
                return None




        if int(s[i:i+3]) <256:

            nl=[]
            if s[i]!='0':
                pl=self.ip(s,i+3,n-1)
                if pl is not None:
                    for p in pl:
                        nl.append(s[i:i+3]+"."+p)
                pl2=self.ip(s,i+2,n-1)
                if pl2 is not None:
                    for p in pl2:
                        nl.append(s[i:i+2]+"."+p)

            pl3=self.ip(s,i+1,n-1)
            if pl3 is not None:
                for p in pl3:
                    print pl3
                    nl.append(s[i]+"."+p)

            return nl
        else:
            nl=[]
            if s[i]!='0':
                pl2=self.ip(s,i+2,n-1)

                if pl2 is not None:
                    for p in pl2:
                        nl.append(s[i:i+2]+"."+p)
            pl3=self.ip(s,i+1,n-1)
            if pl3 is not None:
                for p in pl3:
                    nl.append(s[i]+"."+p)

            return nl



