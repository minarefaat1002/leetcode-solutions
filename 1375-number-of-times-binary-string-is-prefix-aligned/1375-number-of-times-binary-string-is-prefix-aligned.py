class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        Sum = 0
        count = 0
        n = 0
        for i in range(len(flips)):
            Sum += flips[i]
            n = n + i + 1
            if Sum == n :
                count +=1
        return count