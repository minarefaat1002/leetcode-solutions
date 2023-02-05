class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0:
            return False
        count = Counter(nums)
        nums.sort()
        for num in nums:
            if num in count:
                for i in range(num,num+k):
                    if i not in count:
                        return  False
                    count[i]-=1
                    if count[i] == 0:
                        del count[i]
        return True