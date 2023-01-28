class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = [[False]*len(heights[0]) for _ in range(len(heights))]
        atlantic =[[False]*len(heights[0]) for _ in range(len(heights))]
        def dfs1(prev,i,j):
            if i<0 or j < 0 or i==len(heights) or j == len(heights[0]) or (i,j) in visited1 or heights[i][j] < prev:
                return
            visited1.add((i,j))
            pacific[i][j] = True
            dfs1(heights[i][j],i+1,j)
            dfs1(heights[i][j],i,j+1)
            dfs1(heights[i][j],i-1,j)
            dfs1(heights[i][j],i,j-1)
        def dfs2(prev,i,j):
            if i<0 or j < 0 or i==len(heights) or j == len(heights[0]) or (i,j) in visited2 or heights[i][j] < prev:
                return
            visited2.add((i,j))
            atlantic[i][j] = True
            dfs2(heights[i][j],i+1,j)
            dfs2(heights[i][j],i,j+1)
            dfs2(heights[i][j],i-1,j)
            dfs2(heights[i][j],i,j-1)
        visited1 = set()
        visited2 = set()
        for j in range(len(heights[0])):
            if (0,j) not in visited1:
                dfs1(-1,0,j)
        for i in range(len(heights)):
            if (i,0) not in visited1:
                dfs1(-1,i,0)
        for j in range(len(heights[0])):
            if (len(heights)-1,j) not in visited2:
                dfs2(-1,len(heights)-1,j)
        for i in range(len(heights)):
            if (i,len(heights[0])-1) not in visited2:
                dfs2(-1,i,len(heights[0])-1)
        result = []
        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if pacific[i][j] and atlantic[i][j]:
                    result.append([i,j])
        return result