class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set =set()
        for number in nums :
            Set.add(number)
        if len(Set) == len(nums):
            return False 
        return True