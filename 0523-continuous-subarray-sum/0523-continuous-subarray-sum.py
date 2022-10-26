class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # for i in range(len(nums)-1):
        #     Sum = nums[i] + nums[i+1]
        #     if Sum %k == 0:
        #         return True
        #     for j in range(i+2,len(nums)):
        #         Sum+=nums[j]
        #         if Sum%k == 0:
        #             return True
        # return False
    # the above solution time complexity is O(n^2) and it leads to time limit exeeded
        hashmap = {0:-1}
        prefixSum = 0
        for i in range(len(nums)):
            prefixSum+=nums[i]
            if (prefixSum%k in hashmap):
                if (i - hashmap[prefixSum%k] >= 2) :
                    return True
            else:
                hashmap[prefixSum%k] = i
        return False
    # the above solution has time complexity of average O(n)