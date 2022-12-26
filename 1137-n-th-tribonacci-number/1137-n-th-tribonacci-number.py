class Solution:
    def tribonacci(self, n: int) -> int:
        prev = 1
        prevprev = 1
        prevprevprev = 0
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1
        for i in range(3,n+1):
            temp = prev
            prev = prev+prevprev+prevprevprev
            prevprevprev = prevprev
            prevprev=temp
        return prev