class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        hashMap = {}
        for i,num in enumerate(nums):
            hashMap[num] = i
        for operation in operations:
            nums[hashMap[operation[0]]] = operation[1]
            hashMap[operation[1]] = hashMap[operation[0]]
            del hashMap[operation[0]]
        return nums