class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        prefixSum = [0]*len(nums)
        prefixSum[0] = nums[0]
        for i in range(1,len(nums)):
            prefixSum[i] = nums[i] + prefixSum[i-1]
        def sumInRange(left,right):
            if left == 0:
                return prefixSum[right]
            return prefixSum[right] - prefixSum[left-1]
        count = 0
        for i in range(len(nums)-2):
            leftSum = sumInRange(0,i)
            left = i + 1
            right = len(nums) - 2
            seprator1 = -1
            while left <= right:
                mid = (left + right)//2
                if sumInRange(i+1,mid) >= leftSum:
                    seprator1 = mid
                    right = mid - 1
                else:
                    left = mid + 1
            if seprator1 == -1:
                continue 
            left = seprator1
            right = len(nums) - 2
            seprator2 = -1
            while left <= right:
                mid = (left+right)//2
                if sumInRange(i+1,mid) <= sumInRange(mid+1,len(nums)-1):
                    seprator2 = mid
                    left = mid + 1
                else:
                    right = mid -1
            if seprator2 == -1:
                continue
            count+= seprator2 - seprator1 + 1
            count = count % mod 
        return count%mod