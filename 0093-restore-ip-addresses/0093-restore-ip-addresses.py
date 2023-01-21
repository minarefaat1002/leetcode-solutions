class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def dfs(i,temp):
            if i == len(s) and len(temp) == 4:
                res.append(".".join(temp.copy()))
            if i == len(s) or len(temp) >= 4:
                return
            temp.append(s[i])
            dfs(i+1,temp)
            temp.pop()
            if s[i] == "0":
                return
            if i+1 < len(s) :
                temp.append(s[i:i+2])
                dfs(i+2,temp)
                temp.pop()
            if i + 2 < len(s) and int(s[i:i+3]) <= 255:
                temp.append(s[i:i+3])
                dfs(i+3,temp)
                temp.pop()
        dfs(0,[])
        return res