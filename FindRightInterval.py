# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        dic=dict()
        for i,interval in enumerate(intervals):
            dic[interval.start]=i
        startSorted= sorted(dic.keys())

        results=[]
        for interval in intervals:
            endNum=interval.end
            x=self.findClosest(endNum,startSorted,0,len(startSorted)-1)
            if x==None:
                results.append(-1)
            else:
                results.append(dic[x])

        return results

    def findClosest(self,num,sortedList,start,end):

        if end<start:
            return None

        if end==start:
            if sortedList[start]>=num:
                return sortedList[start]
            else:
                return None

        if num>sortedList[(start+end)/2]:
            start=(start+end)/2+1
        else:
            end=(start+end)/2
        return self.findClosest(num,sortedList,start,end)



