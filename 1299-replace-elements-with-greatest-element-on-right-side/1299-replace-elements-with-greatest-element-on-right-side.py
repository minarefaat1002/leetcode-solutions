class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        Max = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = Max
            Max = max(Max,temp)
        return arr