class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = [digit for digit in str(n)]
        res = -1
        Min = "z"
        for i in range(len(s)-1,-1,-1):
            if i == 0:
                return -1
            if s[i] > s[i-1]:
                index = -1
                for j in range(i,len(s)):
                    if s[j] > s[i-1] and s[j] < Min:
                        Min = s[j]
                        index = j
                s[index],s[i-1] = s[i-1],s[index]
                break
        temp = [digit for digit in s[i:]]
        temp.sort()
        return int("".join(s[:i]) + "".join(temp)) if int("".join(s[:i]) + "".join(temp)) <= 2**31 - 1 else -1
