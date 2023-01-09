class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = 1
        for i in range(32):
            setBits = 0
            for j in range(len(candidates)):
                mask = 1
                candidate = candidates[j]
                setBits += candidate&mask
                candidates[j]>>=1
            res = max(res,setBits)
        return res 