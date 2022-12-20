class Solution:
    def minOperations(self, n: int) -> int:
        return int(int(n/2)*(1+2*(int(n/2)-1) + 1 )/2) if n%2 == 0 else int(int(n/2)*(2+2*int(n/2))/2)