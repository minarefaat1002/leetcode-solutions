class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap1 = {}
        hashMap2 = {}
        for i in range(len(s)):
            if (s[i] in hashMap1 and hashMap1[s[i]] != t[i]) or (t[i] in hashMap2 and hashMap2[t[i]]!=s[i]):
                return False
            hashMap1[s[i]] = t[i]
            hashMap2[t[i]] = s[i]
        return True