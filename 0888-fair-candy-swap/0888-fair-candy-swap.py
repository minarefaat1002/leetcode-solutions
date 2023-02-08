class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumAlice = sum(aliceSizes)
        sumBob = sum(bobSizes)
        aliceSizes = set(aliceSizes)
        for s in bobSizes:
            a = (sumAlice - sumBob +2*s)/2
            if a in aliceSizes:
                return [a,s]