class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        pos = [1]*len(nums)
        neg = [1]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    pos[i] = max(pos[i],neg[j] + 1)
                elif nums[i] < nums[j]:
                    neg[i] = max(neg[i],pos[j] + 1)
        return max(max(pos),max(neg))