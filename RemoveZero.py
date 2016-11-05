class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length=len(nums)
        filter(lambda a: a != 0, nums)
        nums=nums+(length-len(nums))*[0]

