class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash2 = {}
        res = collections.defaultdict(list)
        for i,s in enumerate(list2):
            hash2[s] = i
        Min = float('inf')
        for i,s in enumerate(list1):
            if s in hash2:
                Min = min(Min,i+hash2[s])
                res[i+hash2[s]].append(s) 
        return res[Min]
