class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        hashSet =  set(wordDict)
        def dfs(pos,temp):
            if pos == len(s):
                res.append(" ".join(temp))
            for i in range(pos+1,len(s)+1):
                if s[pos:i] in hashSet:
                    temp.append(s[pos:i])
                    dfs(i,temp)
                    temp.pop()
        dfs(0,[])
        return res