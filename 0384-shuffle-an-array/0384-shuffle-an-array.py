class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums
    def shuffle(self) -> List[int]:
        rand_values = [random.random() for i in range(len(self.nums))]
        rand_indexes = [i for i in range(len(self.nums))]
        rand_indexes.sort(key=lambda i:rand_values[i])
        self.nums = [self.nums[i] for i in rand_indexes]
        return self.nums 


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()