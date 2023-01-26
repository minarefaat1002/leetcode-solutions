class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums
    def shuffle(self) -> List[int]:
        shuffled = []
        while len(self.nums) > 0:
            rand_index = random.randrange(0,len(self.nums))
            shuffled.append(self.nums[rand_index])
            self.nums.pop(rand_index)
        self.nums = shuffled
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()