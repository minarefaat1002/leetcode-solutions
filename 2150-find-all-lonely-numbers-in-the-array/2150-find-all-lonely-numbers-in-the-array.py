class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        res = []
        hashMap = Counter(nums)
        for num in nums:
            if hashMap[num] == 1 and (num+1) not in hashMap and (num-1) not in hashMap:
                res.append(num)
        return res