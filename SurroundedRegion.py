class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        if len(board)<=2:
            return
        elif len(board[0])<=2:
            return


        dic={}

        for i in range(len(board)):
            self.island(i,0,board,dic)
            self.island(i,len(board[0])-1,board,dic)

        for j in range(len(board[0])):
            self.island(0,j,board,dic)
            self.island(len(board)-1,j,board,dic)

        for i in range(len(board)):
            for j in range(len(board[0])):

                if str(i)+'-'+str(j) not in dic:
                    board[i][j]='X'








    def island(self,i,j,board,dic):

        if str(i)+'-'+str(j) not in dic:
            if board[i][j]=='0':
                dic[str(i)+'-'+str(j)]=1
                if i!=0:
                    if str(i)+'-'+str(j) not in dic:
                        if board[i][j]=='0':
                            self.island(i-1,j,board,dic)
                if j!=0:
                    if str(i)+'-'+str(j) not in dic:
                        if board[i][j]=='0':
                            self.island(i,j-1,board,dic)
                if i!=len(board)-1:
                    if str(i)+'-'+str(j) not in dic:
                        if board[i][j]=='0':
                            self.island(i+1,j,board,dic)
                if j!=len(board[0])-1:
                    if str(i)+'-'+str(j) not in dic:
                        if board[i][j]=='0':
                            self.island(i,j+1,board,dic)

