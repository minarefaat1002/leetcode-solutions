class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        mapST = {}
        mapTS = {}
        for i in range(len(s)): # for c1,c2 in zip(s,t): # to iterate through two string sameltinously
            c1 = s[i] 
            c2 = t[i]
            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] !=c1)):
                return False
            mapST[c1] = c2
            mapTS[c2] = c1
        return True 