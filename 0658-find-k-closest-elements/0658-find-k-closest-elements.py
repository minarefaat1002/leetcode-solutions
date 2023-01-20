class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0
        r = len(arr)-k
        res = -1
        arr.append(9999999)
        while l <= r:
            mid = (l+r)//2
            if x - arr[mid] > arr[mid+k] - x:
                res = mid + 1
                l = mid + 1
            else:
                r = mid - 1
                res = mid 
        return arr[res:res+k]