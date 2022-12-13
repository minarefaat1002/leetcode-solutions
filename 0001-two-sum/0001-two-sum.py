class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} #val => index
        for  i,n in enumerate(nums): #The count of the current iteration
#The value of the item at the current iteration
            diff =target -n
            if diff in hashmap:
                return [hashmap[diff],i]
            hashmap[n]=i
        return
