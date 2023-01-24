class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0 
        q = deque([[0,0]]) # index ==> jumps
        end = 1
        while q:
            popped = q.popleft()
            for j in range(end,min(nums[popped[0]] + popped[0]+1,len(nums))):
                q.append([j,popped[1]+1])
                if j == len(nums)-1:
                    return popped[1]+1
            end = max(end,nums[popped[0]]+popped[0]+1)