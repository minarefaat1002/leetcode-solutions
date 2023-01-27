class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        i = 0
        while len(arr) != 1:
            del arr[(i + k-1)%len(arr)]
            i = (i+k-1)%(len(arr)+1)
        return arr[0]