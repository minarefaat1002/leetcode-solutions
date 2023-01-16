class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            a = firstList[i]
            b = secondList[j]
            if min(a[1],b[1]) >= max(a[0],b[0]):
                intersection.append([max(a[0],b[0]),min(a[1],b[1])])
            j += 1 if a[1] >= b[1] else 0 
            i += 1 if b[1] >= a[1] else 0
        return intersection