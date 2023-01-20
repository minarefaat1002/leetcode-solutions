class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matches = 0
        countT = Counter(t)
        countS = {}
        j = 0
        i = 0
        res = ""
        for j in range(len(s)):
            if countS.get(s[j],0) == countT.get(s[j],0) - 1:
                matches += 1
            countS[s[j]] = countS.get(s[j],0) + 1
            while matches == len(countT):
                if not res:
                    res = s[i:j+1]
                elif len(res) > j-i+1:
                    res = s[i:j+1]
                if s[i] in countT and countS[s[i]] == countT[s[i]]:
                    matches -= 1
                countS[s[i]] -= 1
                i+=1
        return res