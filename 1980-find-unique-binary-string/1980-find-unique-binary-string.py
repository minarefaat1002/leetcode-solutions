class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        i=0
        res = ""
        for num in nums:
            res+="1" if num[i]=="0" else "0"
            i+=1
        return res 