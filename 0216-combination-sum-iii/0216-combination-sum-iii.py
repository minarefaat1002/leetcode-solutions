class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(k,n,temp,Sum,i):
            if Sum>n or len(temp) > k or i>10:
                return
            if Sum == n and len(temp) == k:
                res.append(temp.copy())
                return
            temp.append(i)
            dfs(k,n,temp,Sum+i,i+1)
            temp.pop()
            dfs(k,n,temp,Sum,i+1)
        dfs(k,n,[],0,1)
        return res