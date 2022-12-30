class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        arr1 = nums.copy()
        while len(arr1) != 1:
            arr2 = [0]*(len(arr1)//2)
            for i in range(len(arr2)):
                if i %2 == 0:
                    arr2[i] = min(arr1[2*i],arr1[2*i+1])
                else:
                    arr2[i] = max(arr1[2*i],arr1[2*i+1])
            arr1 = arr2.copy()
        return arr1[0]