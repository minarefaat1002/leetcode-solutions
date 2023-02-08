class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k or sum(nums)%k !=0 or max(nums) > sum(nums)/k:
            return False
        newK = k
        newNums = []
        Sum = sum(nums)
        for num in nums:
            if num==Sum//k:
                newK-=1
            else:
                newNums.append(num)
        if newK == 0:
            return True
        self.target = sum(newNums)//newK
        used = [False]*16
        newNums.sort(reverse=True)
        def dfs(i,subsetSum,k):
            if k == 1 and subsetSum == self.target:
                return True
            if i==len(newNums) or subsetSum > self.target:
                return False
            if subsetSum == self.target:
                return dfs(0,0,k-1)
            if not used[i]:
                used[i] = True
                if dfs(i+1,subsetSum+newNums[i],k):
                    return True
                used[i] = False
            if dfs(i+1,subsetSum,k):
                return True
        return dfs(0,0,newK)