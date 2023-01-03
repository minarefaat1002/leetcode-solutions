class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        prefixMax = [0]*len(items)
        prefixMax[0] = items[0][1]
        for i in range(1,len(items)):
            prefixMax[i] = max(prefixMax[i-1],items[i][1])
        ans = []*len(queries)
        def getMaxBeauty(query):
            l = 0
            r = len(items) - 1
            res = -1
            while l <= r:
                mid = (l+r)//2
                if items[mid][0] <= query:
                    res = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return prefixMax[res] if res != -1 else 0
        for query in queries:
            maxBeauty = getMaxBeauty(query)
            ans.append(maxBeauty)
        return ans
