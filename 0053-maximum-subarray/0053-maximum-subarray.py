class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxSum = float('-inf')
        # for i in range(len(nums)):
        #     Sum = 0
        #     for j in range(i,len(nums)):
        #         Sum+=nums[j]
        #         maxSum = max(maxSum,Sum)
        # return maxSum
        # The above solution will lead to time limited exeeded cause the time complexity is O(n^2) where n is the length of the array
        maxSum = float('-inf')
        curSum = 0
        for num in nums:
            curSum += num
            maxSum = max(curSum,maxSum)
            if curSum<0:
                curSum = 0
        return maxSum
            
        
        
        '''
        this is the cubic solution and its complexity is O(n^3)
        for(i=0 to n-1)
        for(j=i to n-1)
        for(k=i to j)
        '''
        '''
        this is the quadratic solution and its complexity is O(n^2)
        for(i=0 to n-1)
        for(j=i to n-1)
        curSum+=num[j]
        '''