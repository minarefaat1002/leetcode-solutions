class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashMap = {}
        for domino in dominoes:
            a = domino[0]
            b = domino[1]
            hashMap[(min(a,b),max(a,b))] = hashMap.get((min(a,b),max(a,b)),0) + 1
        count = 0
        for item in hashMap:
            count += int(hashMap[item]*(hashMap[item]-1)/2)
        return count
            