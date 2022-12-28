class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1],[1,1]]
        lasttemp = [1,1]
        if numRows==1:
            return [[1]]
        if numRows ==2 :
            return [[1],[1,1]]
        for i in range(numRows-2):
            temp = [1]
            for j in range(i+1):
                temp.append(lasttemp[j]+lasttemp[j+1])
            temp.append(1)
            res.append(temp)
            lasttemp=temp.copy()
        return res
            