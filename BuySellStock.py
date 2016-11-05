# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]


        maxp=-9e99
        for i in range(len(nums)):

            p=nums[i]
            if p>maxp:
                maxp=p
            for j in range(i+1,len(nums)):
                np=p*nums[j]
                p=np
                if np>maxp:
                    maxp=np

        return maxp


    def maxProduct2(self, nums):

        nnums=0
        for i in nums:
            if nums[i]<0


















        























