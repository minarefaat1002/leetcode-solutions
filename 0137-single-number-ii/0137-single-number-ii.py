class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        sumOfSetBits = 0
        mask = 1
        for i in range(32):
            for num in nums:
                sumOfSetBits += 1 if (num & mask) else 0
            mask = (mask<<1)
            if(sumOfSetBits%3==1):
                result+=2**i
            sumOfSetBits = 0
        for num in nums:
            sumOfSetBits+=1 if (num & mask) else 0
        if sumOfSetBits%3 ==1:
            result = result-(1<<32)  
        return result
                
                

