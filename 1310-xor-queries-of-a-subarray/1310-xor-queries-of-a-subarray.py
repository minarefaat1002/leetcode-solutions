class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefixXor = [0]
        res = []
        xor = 0
        for num in arr:
            xor = num^xor
            prefixXor.append(xor)
        for query in queries:
            L = query[0]
            R = query[1]
            res.append(prefixXor[R+1]^prefixXor[L])
        return res