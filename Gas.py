class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """

        if sum(cost)>sum(gas):
            return -1

        pre=-1
        for p in range(len(gas)):

            if pre!=-1:
                if gas[p]<=cost[p]:
                    pre=-1

            if gas[p]>=cost[p]:
                if self.smaller(gas,cost,p):
                    return p
                else:
                    pre=gas[p]




        return -1



    def smaller(self,list1,list2,p):

        sum1=0
        sum2=0

        for i in range(p,len(list1)):
            sum1=sum1+list1[i]
            sum2=sum2+list2[i]
            if sum2>sum1:
                return False

        for i in range(0,p):
            sum1=sum1+list1[i]
            sum2=sum2+list2[i]
            if sum2>sum1:
                return False
        return True