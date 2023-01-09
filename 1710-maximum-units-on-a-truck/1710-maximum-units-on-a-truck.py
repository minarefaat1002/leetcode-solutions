class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda element: (element[1], element[0]),reverse=True)
        Max = 0
        for box in boxTypes:
            Max += min(box[0],truckSize)*box[1]
            truckSize -= box[0]
            if truckSize <= 0:
                return Max
        return Max