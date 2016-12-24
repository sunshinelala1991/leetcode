import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1


        sorted_dic=sorted(dic.items(), key=operator.itemgetter(1),reverse=True)
        result=[]
        for i in sorted_dic:
            result.append(i)

        return result