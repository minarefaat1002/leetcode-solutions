class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        i = 0
        res = float('inf')
        leftIndex = 0
        while i<len(arr)-1 and arr[i] <= arr[i+1]:
            leftIndex = i + 1
            i+=1
        i = len(arr)-1
        rightIndex = len(arr) - 1
        while i > 0 and arr[i] >= arr[i-1]:
            rightIndex = i - 1
            i-=1
        if rightIndex == 0 or leftIndex == len(arr) - 1:
            return 0
        res = min(len(arr) - leftIndex-1,rightIndex)
        i = 0
        j = rightIndex
        while i <= leftIndex and j<=len(arr)-1:
            if arr[j] < arr[i]:
                j+=1
            elif arr[j] == arr[i]:
                res = min(res,j-i-1)
                i+=1
            else:
                res = min(res,j-i-1)
                i+=1
        return res 