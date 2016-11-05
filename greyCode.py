class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        result=self.code(n)
        for i in range(len(result)):
            result[i]=int(result[i],2)

        return result



    def code(self,n):

        if n==1:
            return ['0','1']


        old_list=self.code(n-1)
        new_list=[]
        for i in range(len(old_list)):
            new_list.append(old_list[i]+'0')

        for i in range(len(old_list)-1,-1,-1):
            new_list.append(old_list[i]+'1')

        return new_list
