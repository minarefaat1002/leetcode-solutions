class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num%2 == 0:
                freq[num] = freq.get(num,0) + 1
        Max = -1
        pivot = -1
        for item in freq:
            if freq[item] == Max:
                pivot = min(pivot,item)
            if freq[item] > Max:
                Max = freq[item]
                pivot = item
        return pivot