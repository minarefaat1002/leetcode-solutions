class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(nums)
        self.tree = [0] + nums.copy()
        for i in range(1,self.N+1):
            j = i + self.LSB(i)
            if j <= self.N:
                self.tree[j] += self.tree[i]
    def LSB(self,num):
        return num & (-num)
    
    def update(self, index: int, val: int) -> None:
        i = index+1
        temp = val
        val = val - self.nums[i-1]
        self.nums[i-1] = temp
        while i <= self.N:
            self.tree[i] = self.tree[i] + val
            i = i + self.LSB(i)
    def prefixSum(self,i):
        i = i + 1
        Sum = 0
        while i > 0:
            Sum = Sum + self.tree[i]
            i = i - self.LSB(i)
        return Sum

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right) - self.prefixSum(left-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)