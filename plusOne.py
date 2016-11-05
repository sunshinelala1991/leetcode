class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result=[]
        flag=False

        for i in range((len(digits)-1),-1,-1):
            if not flag:
                if i == len(digits)-1:
                    s=digits[i]+1
                    if s<10:
                        result=[s]+result
                        flag=False

                    else:
                        result=[s-10]+result
                        flag=True
                else:
                    result=[digits[i]]+result
            else:
                s=digits[i]+1
                if s<10:
                    result=[s]+result
                    flag=False

                else:
                    result=[s-10]+result
                    flag=True

        if flag:
            result=[1]+result

        return result



if __name__=='__main__':
    x=Solution()
    print x.plusOne([])