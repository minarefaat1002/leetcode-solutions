class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def getLps(s):
            lps = [0]*len(s)
            i = 1
            j = 0
            while i < len(s):
                if s[i] == s[j]:
                    j+=1
                    lps[i] = j
                    i+=1
                elif j > 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i+=1
            return lps
        newS = s +"#"+ s[::-1] # to avoid overlap
        lps = getLps(newS)
        return s[lps[-1]:][::-1] + s if s else ""