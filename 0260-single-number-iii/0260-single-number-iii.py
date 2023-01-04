class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor = xor^num
        # the xor result will have at least one set bit 
        mask = 1
        while (xor & mask) == 0:
            mask<<=1
        res = mask
        for num in nums:
            if (mask & num) != 0:
                res = num^res
        n1 = res^mask
        n2 = n1^xor
        return [n1,n2]