class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        maxValue = 0
        for string in strs:
            isString = False
            for char in string:
                if ord(char) - ord('0') > 9:
                    isString = True
                    break
            if isString:
                maxValue = max(maxValue,len(string))
            else:
                maxValue = max(maxValue,int(string))
        return maxValue

