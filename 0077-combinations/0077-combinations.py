class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def dfs(temp,start):
            if len(temp) == k:
                res.append(temp.copy())
                return 
            if start > n:
                return
            for i in range(start,n+1):
                temp.append(i)
                dfs(temp,i+1)
                temp.pop()
        dfs([],1)
        return res