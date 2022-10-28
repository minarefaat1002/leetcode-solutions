class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [1,0]          1---->0 meaning that zero is a prereqisites
        #map each course to prereq list
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        visited = [0]*numCourses
        def dfs(crs):
            if visited[crs]==1:
                return True
            elif visited[crs]==2:
                return
            visited[crs]=1
            for adj in preMap[crs]:
                if dfs(adj):
                    return True
            visited[crs]=2
        for crs in range(numCourses):
            if visited[crs]==0:
                if dfs(crs): return False
        return True 
    