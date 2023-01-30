class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False]*len(arr)
        def dfs(index):
            if index < 0 or index >= len(arr) or visited[index]:
                return False
            if arr[index] == 0:
                return True
            visited[index] = True
            return dfs(index+arr[index]) or dfs(index-arr[index])
        return dfs(start)