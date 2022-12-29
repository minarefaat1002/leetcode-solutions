class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # hashMap = collections.defaultdict(list)
        # res = set()
        # nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         hashMap[nums[i]+nums[j]].append((i,j))
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         rightSide = target - nums[i] - nums[j]
        #         z = 0
        #         while z < len(hashMap[rightSide]):
        #             if rightSide in hashMap and hashMap[rightSide][z][0] not in [i,j] and hashMap[rightSide][z][1] not in [i,j]:
        #                 comb = [nums[i],nums[j],nums[hashMap[rightSide][z][0]],nums[hashMap[rightSide][z][1]]]
        #                 comb.sort()
        #                 res.add(tuple(comb))
        #             z+=1
        # return list(res) 
        res = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue 
                l = j+1
                r = len(nums)-1
                while l < r:
                    if nums[l] + nums[r] == target - nums[i] - nums[j]:
                        res.add((nums[i],nums[j],nums[l],nums[r]))
                        l+=1
                        r-=1
                    elif nums[l] + nums[r] > target - nums[i] - nums[j]:
                        r-=1
                    else:
                        l+=1
        return list(res)