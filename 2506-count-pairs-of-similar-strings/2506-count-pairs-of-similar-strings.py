class Solution:
    def similarPairs(self, words: List[str]) -> int:
        hashMap = {}
        pairs = 0
        for i in range(len(words)):
            charsExists = [False]*26
            for char in words[i]:
                charsExists[ord(char)-ord('a')] = True
            if tuple(charsExists) not in hashMap:
                hashMap[tuple(charsExists)] = 0
            hashMap[tuple(charsExists)] += 1
        for item in hashMap:
            pairs += int(hashMap[item]*(hashMap[item]-1)/2)
        return pairs