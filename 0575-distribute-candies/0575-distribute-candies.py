class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        hashSet = set(candyType)
        return n//2 if len(hashSet) > n//2 else len(hashSet)