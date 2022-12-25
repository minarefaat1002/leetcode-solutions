class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0:
            return False
        dp = set()
        dp.add(0)
        target = sum(nums)//2
        for i in range(len(nums)-1,-1,-1):
            nextdp = set()
            for t in dp:
                if (t + nums[i] <= target): # this if steatment is optional but it saves time 
                    nextdp.add(t+nums[i]) # we cannot iterate this dp set while we're updating it so we make the nextdp set upove 
                nextdp.add(t)
            dp = nextdp
        return True if target in dp else False
    
                