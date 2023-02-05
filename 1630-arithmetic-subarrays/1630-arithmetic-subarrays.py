class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArithmetic(temp):
            diff = temp[1] - temp[0]
            for i in range(1,len(temp)):
                if temp[i] - temp[i-1] != diff:
                    return False 
            return True
        res = []
        for left,right in zip(l,r):
            temp = nums[left:right+1]
            temp.sort()
            if isArithmetic(temp):
                res.append(True)
            else:
                res.append(False)
        return res