class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashSet = set()
        counter = Counter(s)
        count = 0
        res = []
        for char in s:
            hashSet.add(char)
            counter[char]-=1
            if counter[char] == 0:
                hashSet.remove(char)
            count += 1
            if len(hashSet) == 0:
                res.append(count)
                count = 0
        return res