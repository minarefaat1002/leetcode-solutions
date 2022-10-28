class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
#         count=[0]
#         def dp(target,n,k):
#             if n==0 and target==0:
#                 count[0]+=1
#                 return
#             elif n<0 or target<0:
#                 return
#             for i in range(1,k+1):
#                 dp(target-i,n-1,k)
#         dp(target,n,k)
#         return count[0]
# the above solution is so slow and has time limit exeeded .  to improve it we use caching 
        hashMap = {(0,0):1}
        count=[0]
        Mod = 10**9 + 7
        def dp(target,n,k):
            if (target,n) in hashMap:
                return hashMap[(target,n)]
            if n==0 and target==0:
                return 1
            elif n<0 or target<0:
                return 0
            Sum = 0
            for i in range(1,k+1):
                Sum = Sum + (dp(target-i,n-1,k))%Mod
            hashMap[(target,n)] = Sum
            return hashMap[(target,n)]
        return dp(target,n,k) %Mod
