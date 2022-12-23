class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        res = [first]
        for i in range(len(encoded)):
            prev = res[i]
            cur = encoded[i]
            res.append(prev^cur)
        return res
