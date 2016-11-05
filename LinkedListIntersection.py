class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        return self.robbery(nums,len(nums))



    def robbery(self,nums,n):

        if n==0:
            return nums[0]

        if n==1:
            return max(nums[0],nums[1])

        return max(self.robbery(nums,n-1),self.robbery(nums,n-2)+nums[n])




















