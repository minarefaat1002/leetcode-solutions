class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        # o(nlogn) - ---> easy
        # O(n) solution ---- > easy
        i = 0
        j = 0
        Max = 0
        while i<len(nums1) and j<len(nums2):
            if i > j:
                j+=1
            elif nums2[j] >= nums1[i]:
                Max = max(Max,j-i)
                j+=1
            else:
                i+=1
        return Max