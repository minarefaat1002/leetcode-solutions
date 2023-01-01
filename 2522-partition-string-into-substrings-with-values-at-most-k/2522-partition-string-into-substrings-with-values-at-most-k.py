class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        Max = -1
        if k <= 9:
            for char in s:
                Max = max(Max,int(char))
            if Max > k:
                return -1
            else:
                return len(s)
        i = 0
        count = 0
        while i < len(s):
            num = int(s[i])
            if num > k:
                return -1
            if i == len(s) - 1:
                return count+1 if num <= k else -1
            while num < k:
                i+=1
                num = (num*10 + int(s[i])) if i < len(s) else k
            count+=1
        return count 