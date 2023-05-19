class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        endingWithZerosOrOnes = [0]*(high+1)
        endingWithZerosOrOnes[zero] += 1
        endingWithZerosOrOnes[one] += 1
        result = 0
        for i in range(1,high+1):
            if i-zero >= 0 :
                endingWithZerosOrOnes[i] += endingWithZerosOrOnes[i-zero]
            if i-one >= 0:
                endingWithZerosOrOnes[i] += endingWithZerosOrOnes[i-one]

        for i in range(low,high+1):
            result += endingWithZerosOrOnes[i] % MOD
        return result%MOD