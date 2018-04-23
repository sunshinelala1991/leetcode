class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}
        for i in range(len(nums)):
            dic[i]=0


        for i in nums:
            if nums[i] in dic:
                dic[nums[i]]+=1


        for x in dic:
            if dic[x]==0:
                return x

        return nums[-1]+1
