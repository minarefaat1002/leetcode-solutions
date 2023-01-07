class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # hashMap = {}
        # for num in nums:
        #     hashMap[num] = hashMap.get(num,0)+1
        # Max = 0
        # pivot = 0
        # for key in hashMap:
        #     if hashMap[key] > Max:
        #         Max = hashMap[key]
        #         pivot = key
        # return pivot
        # the above solution has average time complexity of O(N) and space complexity of O(N)
        # while True:
        #     count = 0
        #     picked = random.choice(nums)
        #     for num in nums:
        #         if num == picked:
        #             count+=1
        #     if count > int(len(nums)/2):
        #         return picked
        count = 0
        pivot = 0
        for i in range(len(nums)):
            if count==0:
                pivot = nums[i]
                count+=1
            elif pivot == nums[i]:
                count+=1
            else:
                count-=1
        return pivot