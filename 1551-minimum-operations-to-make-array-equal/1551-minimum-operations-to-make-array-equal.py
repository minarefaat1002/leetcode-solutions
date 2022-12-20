class Solution:
    def minOperations(self, n: int) -> int:
        Sum = 0
        for i in range(n):
            Sum += 2*i + 1
        operations = 0
        avg = int(Sum/n)
        for i in range(n):
            if 2*i + 1 < avg:
                operations+= avg - (2*i + 1)
        return operations