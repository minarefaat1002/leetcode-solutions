class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return numOnes-(k-numOnes-numZeros) if k> numOnes+numZeros else min(numOnes,k)