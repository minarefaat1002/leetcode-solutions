class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9+7
        evenPlaces = int(n/2) if n%2 == 0 else int(n/2)+1
        oddPlaces = n-evenPlaces
        return (pow(5,evenPlaces,MOD)*pow(4,oddPlaces,MOD))%(MOD)