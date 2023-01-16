class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 9:
            return 
        hashMap = {}
        res = []
        for i in range(len(s)-9):
            dna = s[i:i+10]
            hashMap[dna] = hashMap.get(dna,0) + 1
        for item in hashMap:
            if hashMap[item] > 1:
                res.append(item)
        return res 