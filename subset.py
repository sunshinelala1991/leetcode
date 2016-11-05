class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)==0:
            return [[]]
        result=self.subset(sorted(nums),len(nums)-1)

        result=sorted(result)

        p=["#"]
        d=[]
        for i in range(len(result)):
            if result[i]!=p:
                d.append(result[i])
            p=result[i]




        return d



    def subset(self,nums,n):
        if n==0:
            return [[],[nums[0]]]

        p_subset=self.subset(nums,n-1)

        n_subset=[]

        for p in p_subset:
            n_subset.append(p+[])
            n_subset.append(p+[nums[n]])

        return n_subset