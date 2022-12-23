class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        counter = [20000]
        visited = set()
        queue = collections.deque()
        queue.append((entrance[0],entrance[1],0))
        while queue:
            popped = queue.popleft()
            r = popped[0]
            c = popped[1]
            if (r,c) in visited:
                continue
            visited.add((r,c))
            if maze[r][c] == "+":
                continue
            curLength = popped[2]
            if (r == 0 or c==0 or r==len(maze)-1 or c == len(maze[0])-1) and curLength and maze[r][c] == ".":
                return curLength
            if r-1 >= 0:
                queue.append((r-1,c,curLength+1))
            if r+1<=len(maze)-1:
                queue.append((r+1,c,curLength+1))
            if c-1 >= 0:
                queue.append((r,c-1,curLength+1))
            if c+1<=len(maze[0])-1:
                queue.append((r,c+1,curLength+1))
        return -1

