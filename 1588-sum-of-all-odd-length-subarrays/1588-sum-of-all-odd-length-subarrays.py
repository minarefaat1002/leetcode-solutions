class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        Sum = 0
        for i in range(len(arr)):
            left = i+1
            right = len(arr)-i
            noOfSubarrays = left*right
            noOfSubarrays = int(noOfSubarrays/2) if noOfSubarrays%2 ==0 else int(noOfSubarrays/2)+1
            Sum += noOfSubarrays*arr[i]
        return Sum