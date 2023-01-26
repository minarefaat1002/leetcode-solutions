class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        kept = set()
        def dfs(i,j):
            if i < 0 or j < 0 or i == len(board) or j == len(board[0]) or board[i][j] == "X" or (i,j) in visited:
                return
            visited.add((i,j))
            if board[i][j] == "O":
                kept.add((i,j))
            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        for i in range(len(board)):
            if (i,0) not in visited and board[i][0] == "O":
                dfs(i,0)
            if (i,len(board[0])-1) not in visited and board[i][-1] == "O":
                dfs(i,len(board[0])-1)
        for j in range(len(board[0])):
            if (0,j) not in visited and board[0][j] == "O":
                dfs(0,j)
            if (len(board[0])-1,j) not in visited and board[-1][j] == "O":
                dfs(len(board)-1,j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in kept:
                    board[i][j] = "X"
        
                    