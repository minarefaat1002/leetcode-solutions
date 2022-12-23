class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        leftMost = -1
        rightMost = -1
        for i in range(len(s)):
            if s[i] == "1":
                if leftMost == -1:
                    leftMost = i
                rightMost = i
        for i in range(leftMost,rightMost):
            if s[i] == "0":
                return False
        return True