class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(arr,key=lambda num:[abs(num-x),num])[:k])
        