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
    #     hashmap = {n:1}
    #     def dfs(i):
    #         if i>n:
    #             return 0
    #         if i in hashmap:
    #             return hashmap[i]
    #         hashmap[i] = dfs(i+1) + dfs(i+2)
    #         return hashmap[i]
    #     return dfs(0)
    # # the above solution is an improvement of the first solution and it has time complexity of O(n) and space complexity of O(n)
        first = 1
        if n == 1:
            return first
        second = 2
        for i in range(3,n+1):
            temp = second 
            second = first + second 
            first = temp
        return second