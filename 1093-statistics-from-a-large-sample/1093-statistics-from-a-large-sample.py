class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        Max = float('-inf')
        Min = float('inf')
        c = 0
        Sum = 0
        maxFreq = -1
        maxFreqEle = None
        for i in range(len(count)):
            if count[i] > maxFreq:
                maxFreq = count[i]
                maxFreqEle = i
            if count[i] > 0:
                Max = max(Max,i)
                Min = min(Min,i)
            Sum += i*count[i]
            c+= count[i]
        mean = Sum/c
        i = 0
        cnt = 0
        middle = int(c/2)
        median = 0
        if c%2 == 1:
            while True:
                cnt+=count[i]
                if cnt >= middle+1:
                    median = i
                    break
                i+=1
        else:
            while True:
                cnt+=count[i]
                if cnt > middle:
                    median = i*2
                    break
                elif cnt == middle:
                    median+=i
                    i+=1
                    while count[i] == 0:
                        i+=1
                    median+=i
                    break
                i+=1
            median = median/2
        return [Min,Max,mean,median,maxFreqEle]