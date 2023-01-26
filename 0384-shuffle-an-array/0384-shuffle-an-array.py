'''
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
'''
'''
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
'''
class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums
    def shuffle(self) -> List[int]:
        last_index = len(self.nums)-1
        while last_index:
            rand_index = random.randint(0,last_index)
            temp = self.nums[last_index]
            self.nums[last_index] = self.nums[rand_index]
            self.nums[rand_index] = temp
            last_index-=1
        return self.nums
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
