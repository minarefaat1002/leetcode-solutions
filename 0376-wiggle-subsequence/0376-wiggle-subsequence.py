class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # this solution is similar to longest increasing subsequence problem
        # pos = [1]*len(nums)
        # neg = [1]*len(nums)
        # for i in range(1,len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             pos[i] = max(pos[i],neg[j] + 1)
        #         elif nums[i] < nums[j]:
        #             neg[i] = max(neg[i],pos[j] + 1)
        # return max(max(pos),max(neg))
        pos = [1]*len(nums)
        neg = [1]*len(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                pos[i] = neg[i-1] + 1
                neg[i] = neg[i-1]
            elif nums[i] < nums[i-1]:
                neg[i] = pos[i-1] + 1
                pos[i] = pos[i-1]
            else:
                neg[i] = neg[i-1]
                pos[i] = pos[i-1]
        return max(max(pos),max(neg))