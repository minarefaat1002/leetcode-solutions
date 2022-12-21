class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        sumOfArray = sum(arr)
        if sumOfArray%3 != 0:
            return False
        Sum = 0
        count = 0
        for i in range(len(arr)):
            Sum+=arr[i]
            if Sum == int(sumOfArray/3):
                Sum = 0
                count+=1
        return True if count >= 3 else False