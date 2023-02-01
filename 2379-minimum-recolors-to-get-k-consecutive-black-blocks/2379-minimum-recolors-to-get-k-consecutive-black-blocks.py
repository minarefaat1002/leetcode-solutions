class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = 0
        for i in range(k):
            count += 1 if blocks[i] == "W" else 0
        res = count
        for i in range(k,len(blocks)):
            if blocks[i] == "W":
                count+=1
            if blocks[i-k] == "W":
                count -= 1
            res = min(res,count)
        return res