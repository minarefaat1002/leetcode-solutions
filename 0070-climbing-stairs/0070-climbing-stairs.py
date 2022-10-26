class Solution:
    def climbStairs(self, n: int) -> int:
    #     def dfs(i):
    #         if i>n:
    #             return 0
    #         if i==n:
    #             return 1
    #         return dfs(i+1) + dfs(i+2)
    #     return dfs(0)
    # # tiem complexity of this solution is O(2^n) and it will lead to time limit exeeded
        hashmap = {n:1}
        def dfs(i):
            if i>n:
                return 0
            if i in hashmap:
                return hashmap[i]
            hashmap[i] = dfs(i+1) + dfs(i+2)
            return hashmap[i]
        return dfs(0)