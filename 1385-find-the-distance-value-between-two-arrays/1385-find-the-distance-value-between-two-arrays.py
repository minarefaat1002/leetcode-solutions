class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # arr1[i] - arr2[j] <= d
        # # arr1[i] - arr2[j] >= d
        def isThereAnElement(ele):
            l = 0 
            r = len(arr2) - 1
            while l<=r:
                mid = (l+r)//2
                if abs(ele - arr2[mid]) <= d:
                    return True
                elif ele - arr2[mid] > d:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        arr2.sort()
        count = 0
        for ele in arr1:
            if not isThereAnElement(ele):
                count += 1
        return count