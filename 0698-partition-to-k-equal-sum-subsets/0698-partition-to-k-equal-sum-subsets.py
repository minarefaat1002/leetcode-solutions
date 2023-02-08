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
        newNums.sort(reverse = True )
        dp = {}
        self.target = sum(newNums)//newK
        used = [False]*16
        newNums.sort(reverse=True)
        def dfs(i,subsetSum,k):
            if (tuple(used),k) in dp:
                return dp[(tuple(used),k)]
            if k == 1 and subsetSum == self.target:
                return True
            if i==len(newNums) or subsetSum > self.target:
                return False
            if subsetSum == self.target:
                dp[(tuple(used),k)] = dfs(0,0,k-1)
                return dp[(tuple(used),k)]
            if not used[i]:
                used[i] = True
                dp[(tuple(used),k)] = dfs(i+1,subsetSum+newNums[i],k)
                if dp[(tuple(used),k)]:
                    return True
                used[i] = False
            dp[(tuple(used),k)] = dfs(i+1,subsetSum,k)
            if dp[(tuple(used),k)]:
                return True
        return dfs(0,0,newK)