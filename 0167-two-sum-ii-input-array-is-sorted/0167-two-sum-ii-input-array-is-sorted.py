class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1,len(numbers)):
        #         if numbers[i]+numbers[j] == target:
        #             return [i+1,j+1]
        # return -1
        # the above solution will lead to time limit exeeded cause the time complexity is : O(n^2)
        l = 0
        r = len(numbers)-1
        Sum = numbers[l]+numbers[r]
        while l<r:
            Sum = numbers[l]+numbers[r]
            if Sum ==target:
                return [l+1,r+1]
            elif Sum > target:
                r-=1
            else:
                l+=1
        # the above solution has time complexity O(n) --->cause we make a single iteration