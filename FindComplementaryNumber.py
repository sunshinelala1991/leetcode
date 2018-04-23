class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """

        biFormat= "{0:b}".format(num)
        newString=''
        for i, c in enumerate(biFormat):
            if(c=='0'):
                newString+='1'
            else:
                newString+='0'

        return int(newString, 2)







s= Solution()
s.findComplement(5)