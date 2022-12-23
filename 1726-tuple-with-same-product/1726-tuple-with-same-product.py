class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = 0
        multiplications = {}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                multiplications[nums[i]*nums[j]] = multiplications.get(nums[i]*nums[j] , 0)+1
        for item in multiplications:
            count += multiplications[item]*(multiplications[item]-1)
        return count*4
