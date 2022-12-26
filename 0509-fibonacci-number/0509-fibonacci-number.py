class Solution:
    def fib(self, n: int) -> int:
        memo =[0,1]
        if n == 0:
            return 0
        for i in range(2,n+1):
            memo.append(memo[i-1]+memo[i-2])
        return memo[-1]
    '''
    def fib(self, n: int) -> int:
        if n==1:
            return 1
        if n ==0:
            return 0
        return self.fib(n-1) + self.fib(n-2)
    '''