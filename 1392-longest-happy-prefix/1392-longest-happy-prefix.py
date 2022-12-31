class Solution:
    def longestPrefix(self, s: str) -> str:
        def getLps(s):
            lps = [0]*len(s)
            i = 1
            j = 0 
            while i < len(s):
                if s[i] == s[j]:
                    j += 1
                    lps[i] = j
                    i+=1
                elif j > 0:
                    j = lps[j-1]
                else:
                    lps[i] = 0
                    i+=1
            return lps[-1]
        n = getLps(s)
        return s[:n]