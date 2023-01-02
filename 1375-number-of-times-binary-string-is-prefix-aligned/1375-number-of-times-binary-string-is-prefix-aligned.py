class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        Sum = 0
        count = 0
        for i in range(len(flips)):
            Sum += flips[i]
            if Sum == (i+1)*(i+2)//2 :
                count +=1
        return count 