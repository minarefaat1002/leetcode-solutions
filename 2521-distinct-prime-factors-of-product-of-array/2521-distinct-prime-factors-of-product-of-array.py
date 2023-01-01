class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime = True
        Set = set()
        for num in nums:
            for i in range(2,int(sqrt(num))+2):
                while num%i == 0:
                    Set.add(i)
                    num = num//i
            if num != 1:
                Set.add(num)
        return len(Set)