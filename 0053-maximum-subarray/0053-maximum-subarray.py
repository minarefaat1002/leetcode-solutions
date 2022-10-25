class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
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