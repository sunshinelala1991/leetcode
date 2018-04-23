class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        lengthB=len(b)
        dic={}
        result=1
        a%=1337
        result10=a
        for i,pow in enumerate(b[::-1]):
            if i!=0:
                result10=result10**10%1337

            result=result*(result10**pow)%1337
            if result>1337:
                result%=1337
            if result==0:
                return 0

        return result




