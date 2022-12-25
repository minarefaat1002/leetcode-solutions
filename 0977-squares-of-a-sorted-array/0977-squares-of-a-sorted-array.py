
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i] = nums[i]*nums[i]
        # nums.sort()
        # return nums
        # the above solution has time complexity of O(nlogn)
        # arr = [0]*10001
        # for num in nums:
        #     arr[abs(num)]+=1
        # newNums = []
        # for i in range(len(arr)):
        #     while arr[i]:
        #         newNums.append(i*i)
        #         arr[i]-=1
        # return newNums
        # the above solution has time complexity of O(N) where N is 10^4
        newNums = []
        l = 0
        r = len(nums)-1
        while l<=r:
            if abs(nums[l]) >= abs(nums[r]):
                newNums.append(nums[l]*nums[l])
                l+=1
            else:
                newNums.append(nums[r]*nums[r])
                r-=1
        return newNums[::-1]
        # the above solution has time complexity of O(N) where N is the length of the array nums