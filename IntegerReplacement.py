class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """

        return self.replace(n)


    def replace(self, n):
        if n==1:
            return 0
        elif n%2==0:
            return self.replace(n/2)+1
        else:
            return min(self.replace(n+1),self.replace(n-1))+1