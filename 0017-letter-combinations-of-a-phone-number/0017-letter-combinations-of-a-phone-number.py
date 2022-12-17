class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashmap ={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        temp = []
        res=[]
        def dfs(i):
            if i ==len(digits):
                res.append("".join(temp.copy()))
                return
            for z in range(len(hashmap[int(digits[i])])):
                temp.append(hashmap[int(digits[i])][z])
                dfs(i+1)
                temp.pop()
        dfs(0)
        return res if res[0] !="" else [] # this line to handle the case [""]
    # the time complexity is O(n*4^n)