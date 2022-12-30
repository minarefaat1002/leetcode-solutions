class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # count = [0]*(len(nums)+1)
        # res=[]
        # for num in nums:
        #     count[num]+=1
        # for i in range(1,len(count)):
        #     if count[i] == 0:
        #         res.append(i)
        # return res
        # the above solution has time and space complexity of O(N) where N is the length of the array nums
        res = []
        for i in range(len(nums)):
            nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
        # The above solution has time complexity of O(N) it uses no extra space complexity