class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hashMap = {0:1}
        curSum = 0
        count = 0
        for num in nums:
            curSum += num
            if  curSum%k in hashMap:
                count += hashMap[curSum%k]
            hashMap[curSum%k] = hashMap.get(curSum%k,0) + 1
        return count 