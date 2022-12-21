class Solution:
    def smallestValue(self, n: int) -> int:
        def notPrime(n):
            for i in range(2,int(sqrt(n)+1)):
                if n%i == 0:
                    return True
            return False
        def primeFactors(n):
            Sum = 0
            i = 2
            while n != 1:
                while n % i == 0:
                    Sum += i
                    n = int(n/i)
                i+=1
            return Sum
        while notPrime(n):
            nn = primeFactors(n)
            if n == nn:
                break
            n = nn
        return n
        