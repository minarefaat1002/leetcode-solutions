class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evenPointer = 0
        oddPointer = 1
        while( evenPointer < len(nums) and oddPointer < len(nums)):
            if(not nums[evenPointer]%2):
                evenPointer+=2
            elif(nums[oddPointer]%2):
                oddPointer+=2
            else:
                temp = nums[evenPointer]
                nums[evenPointer] = nums[oddPointer]
                nums[oddPointer] = temp
        return nums