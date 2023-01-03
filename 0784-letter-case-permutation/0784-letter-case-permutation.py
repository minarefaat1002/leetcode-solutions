class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(i,temp):
            if len(temp) == len(s):
                res.append("".join(temp.copy()))
                return
            if s[i].isdigit():
                temp.append(s[i])
                dfs(i+1,temp)
                temp.pop()
            else:
                temp.append(s[i].lower())
                dfs(i+1,temp)
                temp.pop()
                temp.append(s[i].upper())
                dfs(i+1,temp)
                temp.pop()
        dfs(0,[])
        return res