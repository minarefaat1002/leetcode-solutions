class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        hashMap = collections.defaultdict(list)
        Min = float('inf')
        for i,card in enumerate(cards):
            hashMap[card].append(i)
        for item in hashMap:
            for i in range(1,len(hashMap[item])):
                Min = min(Min,hashMap[item][i] - hashMap[item][i-1]+1)
        return Min if Min != float('inf') else -1
