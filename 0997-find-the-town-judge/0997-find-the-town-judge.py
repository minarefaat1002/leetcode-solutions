class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = [0]*(n+1)
        pivot = -1
        for i in range(len(trust)):
            arr[trust[i][1]]+=1
        for i in range(1,len(arr)):
            if arr[i] == n-1:
                pivot = i
        for pair in trust:
            if pair[0] == pivot:
                pivot = -1
        return pivot
        