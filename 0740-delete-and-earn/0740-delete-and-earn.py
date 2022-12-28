class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = [0]*10001
        prev = 0
        prevprev = 0
        cur = 0
        for num in nums:
            count[num] += 1
        for i in range(1,len(count)):
            temp = prev
            if count[i] == 0:
                continue
            elif count[i-1] > 0:
                prev = max(count[i]*i + prevprev,prev)
            else:
                prev = max(count[i]*i + prev,prev)
            prevprev = temp
        return prev
                
                