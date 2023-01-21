class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        subBoxes = collections.defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != ".":
                    if i not in rows:
                        rows[i] = set()
                    if j not in cols:
                        cols[j] = set()
                    if (i//3,j//3) not in subBoxes:
                        subBoxes[(i//3,j//3)] = set()
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    subBoxes[(i//3,j//3)].add(board[i][j])
        res = [[] for _ in range(9)]
        def dfs(i,j):
            if i == 9 and j == 0:
                return True
            if j == 9:
                if dfs(i+1,0):
                    return True
                return
            if board[i][j] == ".":
                for z in range(1,10):
                    z = str(z)
                    if z not in rows[i] and z not in cols[j] and z not in subBoxes[(i//3,j//3)]:
                        rows[i].add(z)
                        cols[j].add(z)
                        subBoxes[(i//3,j//3)].add(z)
                        board[i][j] = z
                        if dfs(i,j+1):
                            return True
                        rows[i].remove(z)
                        cols[j].remove(z)
                        subBoxes[(i//3,j//3)].remove(z)
                board[i][j] = "."
            else:
                if dfs(i,j+1):
                    return True
        dfs(0,0)