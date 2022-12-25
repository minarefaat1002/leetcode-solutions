class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        if not s:
            return True
        for letter in t:
            if i == len(s): 
                return True  # If match full s -> then s is a subsequence
            if  s[i] == letter:
                i+=1
        return i == len(s)