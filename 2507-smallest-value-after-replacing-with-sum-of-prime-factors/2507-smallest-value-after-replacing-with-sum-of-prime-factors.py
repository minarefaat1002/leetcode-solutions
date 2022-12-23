class Solution:
    def smallestValue(self, n: int) -> int:
        def primeFactors(n):
            Sum = 0
            for i in range(2,int(sqrt(n))+1):
                while n % i == 0:
                    Sum += i
                    n = int(n/i)
            Sum += n if n != 1 else 0
            return Sum
        while True:
            sumOfFactors = primeFactors(n)
            if n == sumOfFactors:
                return n
            n = sumOfFactors
        