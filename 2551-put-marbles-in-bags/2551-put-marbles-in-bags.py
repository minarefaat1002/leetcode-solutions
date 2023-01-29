class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        total = weights[0] + weights[-1]
        arr = []
        for i in range(len(weights)-1):
            arr.append(weights[i]+weights[i+1])
        arr.sort()
        return sum(arr[len(arr)-k+1:]) - sum(arr[:k-1]) 