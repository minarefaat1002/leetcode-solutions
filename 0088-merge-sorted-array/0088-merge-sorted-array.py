class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     j = 0
    #     for i in range(m,m+n):
    #         nums1[i] = nums2[j]
    #         j+=1
    #     return nums1.sort()
    # # the above solution has time complexity of O(nlogn)
        i = m-1
        j = n-1
        while i>=0 and j>=0:
            if nums2[j] > nums1[i]:
                nums1[i+j+1] = nums2[j]
                j-=1
            else:
                nums1[i+j+1] = nums1[i]
                i-=1
        if j>=0:
            for x in range(j,-1,-1):
                nums1[x] = nums2[x]
        return nums1
    # time complexity of the above solution is O(n+m)