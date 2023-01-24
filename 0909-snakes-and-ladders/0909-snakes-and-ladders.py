class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        def valToPos(square):
            r = (square-1)//n
            c = (square-1)%n if r%2 == 0 else n-(square-1)%n - 1
            return [r,c]
        q = deque()
        q.append([1,0]) # square ===> moves
        visited = set()
        visited.add(1)
        board.reverse()
        n = len(board)
        while q:
            square,moves = q.popleft()
            for i in range(1,7):
                nextSquare = square + i
                r,c = valToPos(nextSquare)
                if board[r][c] != -1:
                    nextSquare = board[r][c]
                if nextSquare not in visited:
                    q.append([nextSquare,moves+1])
                    visited.add(nextSquare)
                if nextSquare == n*n:
                    return moves + 1
        return -1
                
            