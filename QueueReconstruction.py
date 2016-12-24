class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:
            return 0
        nums=sorted(nums)

        median=nums[len(nums)/2]

        result=0

        for n in nums:
            result+=abs(median-n)


        return result













