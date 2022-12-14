class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # if even then 0
        # if odd then num
        len1 = len(nums1)
        len2 = len(nums2)
        xor = 0
        if len2%2 != 0:
            for num in nums1:
                xor = xor^num
        if len1%2 !=0:
            for num in nums2:
                xor = xor^num
        return xor