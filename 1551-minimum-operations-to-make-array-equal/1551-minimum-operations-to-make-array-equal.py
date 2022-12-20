class Solution:
    def minOperations(self, n: int) -> int:
        avg = int((n*(1 + 2*(n-1) + 1)/2)/n)
        operations = 0
        for i in range(n):
            if 2*i + 1 < avg:
                operations+= avg - (2*i + 1)
        return operations