class Solution(object):
    def solve(self, board):
        
        for i in [0, len(board)-1]:
            for j in range(0, len(board[0])):
                if(board[i][j] == "O"):
                    self.dfs(i, j, board)
        
        for i in range(0, len(board)):
            for j in [0, len(board[0])-1]:
                if(board[i][j] == "O"):
                    self.dfs(i, j, board)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if(board[i][j] == "O"):
                    board[i][j] = "X"
                if(board[i][j] == "Y"):
                    board[i][j] = "O"


    def dfs(self, i, j, board):
        if(i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != "O"):
            return
        
        board[i][j] = "Y"

        self.dfs(i-1, j, board)
        self.dfs(i, j-1, board)
        self.dfs(i, j+1, board)
        self.dfs(i+1, j, board)