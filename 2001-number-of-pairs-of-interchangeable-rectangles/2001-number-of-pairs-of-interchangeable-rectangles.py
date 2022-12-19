class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hashMap = {}
        for rect in rectangles:
            width = rect[0]
            height = rect[1]
            ratio = width / height
            hashMap[ratio] = hashMap.get(ratio,0) + 1
        Sum = 0
        for item in hashMap:
            Sum += hashMap[item]*(hashMap[item]-1)/2
        return int(Sum)