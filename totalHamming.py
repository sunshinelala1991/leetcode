class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 or len(nums)==1:
            return 0

        t=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):

                s1="{0:b}".format(nums[i])
                s2="{0:b}".format(nums[j])
                t+=self.hamming(s1,s2)

        return t



    def hamming(self,s1,s2):

        if len(s1)>len(s2):
            s2=(len(s1)-len(s2))*'0'+s2
        else:
            s1=(len(s2)-len(s1))*"0"+s1

        d=0
        for a,b in zip(s1,s2):
            if a!=b:
                d+=1

        return d



s=Solution();
print s.totalHammingDistance([4,14,2])

