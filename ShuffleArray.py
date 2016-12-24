class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """


        dic={}
        counts={}

        for i,c in enumerate(s):
            if c not in dic:
                dic[c]=[]
                counts[c]=0

            dic[c].append(i)
            counts[c]+=1

        p=-1



        for c in t:
            if c not in dic:
                return False

            if counts[c]<0:
                return False

            np=dic[c][len(dic[c])-counts[c]]
            counts[c]-=1

            if np<=p:
                return False

            p=np

        return True











# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()