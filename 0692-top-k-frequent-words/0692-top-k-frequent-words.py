class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        wordsCounter = []
        res = []
        for word in counter:
            wordsCounter.append([-counter[word],word])
        heapq.heapify(wordsCounter)
        while k:
            res.append(heapq.heappop(wordsCounter)[1])
            k-=1
        return res