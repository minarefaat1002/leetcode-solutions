class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        minStack = []
        Sum = 0
        for i in range(len(nums)-1,1,-1):
            if minStack:
                minStack.append(min(minStack[-1],nums[i]))
            else:
                minStack.append(nums[i])
        Max = nums[0]
        for i in range(1,len(nums)-1):
            if Max < nums[i] and nums[i] < minStack[-1]:
                Sum +=2
            elif nums[i-1] < nums[i] and nums[i] < nums[i+1]:
                Sum+=1
            Max = max(Max,nums[i])
            minStack.pop()
        return Sum