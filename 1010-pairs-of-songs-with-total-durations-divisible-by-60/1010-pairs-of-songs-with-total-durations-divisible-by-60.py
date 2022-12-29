class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        arr = [0]*60
        counter = 0
        for i in range(len(time)):
            remainder = time[i]%60
            if remainder == 0:
                counter+=arr[0]
            else:
                counter += arr[60-remainder]
            arr[remainder]+=1
        return counter