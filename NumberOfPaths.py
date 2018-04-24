class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        M=10**9+7
        if N==0:
            return 0
        oldPathArray=[]
        for x in range(m+2):
            oldPathArray.append([0]*(n+2))
        for y in range(1,n+1):
            oldPathArray[1][y]+=1
            oldPathArray[m][y]+=1

        for x in range(1,m+1):
            oldPathArray[x][1]+=1
            oldPathArray[x][n]+=1

        result=oldPathArray[i+1][j+1]
        for x in range(1,N):
            newPathArray=[]
            newPathArray.append([0]*(n+2))
            for row in range(1,m+1):
                newPathArray.append([0])
                for col in range(1,n+1):
                    newPathArray[row].append((oldPathArray[row-1][col]
                                              +oldPathArray[row+1][col]+
                                              oldPathArray[row][col+1]+
                                              oldPathArray[row][col-1])%M)
                newPathArray[row].append(0)
            newPathArray.append([0]*(n+2))
            result+=newPathArray[i+1][j+1]
            result%=M
            oldPathArray=newPathArray

        return result