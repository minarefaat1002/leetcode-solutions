class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result =1 
        for num in nums:
            if num==0:
                return 0
            elif num<0:
                result =result*-1
            else:
                result = result*1
        return result 