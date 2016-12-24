class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """



        if len(board)==0:
            return 0

        if len(board[0])==0:
            return 0

        newBoard=[]

        for i in range(len(board)):
            newBoard.append([])
            for j in range(len(board[0])):

                if i==0 and j>0:
                    if board[i][j-1]=="X":
                        newBoard[i].append(".")
                        continue
                if j==0 and i>0:
                    if board[i-1][j]=="X":
                        newBoard[i].append(".")
                        continue
                if i>0 and j>0:
                    if board[i-1][j]=="X" or board[i][j-1]=="X":
                        newBoard[i].append(".")
                        continue
                newBoard[i].append(board[i][j])
        count=0
        for row in newBoard:
            for j in row:
                if j=="X":
                    count+=1

        return count



