class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        sumDifference = 0
        mod = 10**9 + 7
        for i in range(len(nums1)):
            sumDifference += abs(nums1[i] - nums2[i])
        sortedNums1 = sorted(nums1)
        maxSaved = 0
        for i in range(len(nums1)):
            minAbsSum = curAbsSum = abs(nums1[i] - nums2[i])
            left = 0
            right = len(nums1) - 1
            while left <= right:
                mid  = (left+right)//2
                minAbsSum = min(minAbsSum,abs(sortedNums1[mid]-nums2[i]))
                if sortedNums1[mid] >= nums2[i]:
                    right = mid - 1
                else:
                    left = mid + 1
            maxSaved = max(maxSaved,curAbsSum - minAbsSum)
        return (sumDifference - maxSaved)%mod