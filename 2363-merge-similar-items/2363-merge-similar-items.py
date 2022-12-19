class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        hashMap = {}
        ret = []
        for item in items1:
            hashMap[item[0]] = hashMap.get(item[0],0) + item[1]
        for item in items2:
            hashMap[item[0]] = hashMap.get(item[0],0) + item[1]
        for item in hashMap:
            ret.append([item,hashMap[item]])
        ret.sort()
        return ret