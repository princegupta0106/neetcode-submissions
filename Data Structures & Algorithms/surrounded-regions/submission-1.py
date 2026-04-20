class Solution:
    def solve(self, board: List[List[str]]) -> None:
       
        m = len(board)
        n =len(board[0])


        def change(i, j):
            if  i < 0 or j < 0 or i ==m or j ==n or board[i][j] == "X" or board[i][j] == "t":
                return 
            board[i][j] = "t"
            change(i+1,j)
            change(i-1,j)
            change(i,j+1)
            change(i,j-1)
            return 

        for i in range (m):
            if board[i][0] == "O":
                change(i,0)
            if board[i][n-1] == "O":
                change(i,n-1)
        for j in range (n):
            if board[0][j] == "O":
                change(0,j)
            if board[m-1][j]== "O":
                change(m-1,j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "t":
                    board[i][j] = "O"

            
                  
            




        