class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]
        hashMap = collections.defaultdict(list)
        first = None
        res = []
        for pair in adjacentPairs:
            hashMap[pair[0]].append(pair[1])
            hashMap[pair[1]].append(pair[0])
        for item in hashMap:
            if len(hashMap[item]) == 1:
                first = item 
                break
        res.append(first)
        res.append(hashMap[first][0])
        cur = hashMap[first][0]
        del hashMap[first]
        while len(res) != len(adjacentPairs):
            if hashMap[cur][0] == res[-2]:
                res.append(hashMap[cur][1])
                temp = cur
                cur = hashMap[cur][1]
                del hashMap[temp]
            else:
                res.append(hashMap[cur][0])
                temp = cur
                cur = hashMap[cur][0]
                del hashMap[temp]
        if hashMap[cur][0] == res[-2]:
            res.append(hashMap[cur][1])
        else:
            res.append(hashMap[cur][0])
        return res