class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def dfs(pos):
            if pos == len(word):
                return True
            if pos in memo:
                return memo[pos]
            for i in range(pos+1,len(word)+1):
                if word[pos:i] in hashSet and dfs(i):
                    memo[pos] = True
                    return memo[pos]
            memo[pos] = False
            return memo[pos]
            
                        
        hashSet = set(words)
        res = []
        for word in words:
            memo = {}
            hashSet.remove(word)
            if dfs(0):
                res.append(word)
            hashSet.add(word)
        return res