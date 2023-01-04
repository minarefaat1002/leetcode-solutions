class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        res = len(words)
        i = startIndex
        for i in range(len(words)):
            if words[i] == target:
                res = min(res,abs(i-startIndex),len(words) - abs(i-startIndex))
        return res if res != len(words) else -1