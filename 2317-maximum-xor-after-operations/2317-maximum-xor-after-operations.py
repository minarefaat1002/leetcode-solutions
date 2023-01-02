class Solution:
    def maximumXOR(self, nums: List[int]) -> int:
        # a = nums[i] , x = x
        # a.(a xor b)
        # a.(a.b' + a'b)
        # a.a.b' + a.a'.b
        # a.b' will result less or equal number always
        # nums[i] AND x'
        # 0001
        # 0010
        # 0010
        # 0011
        # 1001
        Or = 0
        for num in nums:
            Or = Or | num
        return Or