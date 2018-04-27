class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix)==0 or len(matrix[0])==0:
            return False

        i=0
        j=0
        if matrix[0][0]>target:
            return False

        direction=0
        m=len(matrix)
        n=len(matrix[0])
        while i>=0 and j>=0 and i<m and j<n:
            if matrix[i][j]==target:
                return True



            if direction==0:
                if i+1<m:
                    if matrix[i+1][j]>target:
                        direction=1
                    else:
                        i+=1
                else:direction=1

            elif direction==1:
                if j+1<n:
                    if matrix[i][j+1]>target:
                        direction=2
                    else:
                        j+=1
                else:
                    return False
            else:
                if i-1>=0:
                    i-=1
                    direction=1
                else:
                    return False

        return False







