import math
import Queue
class Solution(object):
    def numSquares(self, n):

        if n<2:
            return n


        squareList=[]

        for i in range(1, int(math.sqrt(n))+1):
            squareList.append(i*i)

        nodeList=[n]

        count=0

        while True:
            newNodeList=[]
            count+=1
            for node in nodeList:
                for x in squareList:
                    y=node-x
                    if y>0:
                        newNodeList.append(y)
                    elif y==0:
                        return count
                    else:
                        break
            nodeList=newNodeList













