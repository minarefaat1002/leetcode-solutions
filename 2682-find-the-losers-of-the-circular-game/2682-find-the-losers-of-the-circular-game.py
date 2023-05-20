class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        arr = [0]*n
        i = 0
        step = 1
        res = []
        while arr[i] == 0:
            arr[i] = 1
            i = (i+step*k+n)%n
            step+=1
        for i in range(n):
            if arr[i] == 0:
                res.append(i+1)
        return res
        