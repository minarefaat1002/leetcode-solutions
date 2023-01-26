class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        hashMap = {}
        for i,char in enumerate(order):
            hashMap[char] = i
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j ==  len(words[i+1]) or hashMap[words[i][j]] > hashMap[words[i+1][j]]:
                    return False
                if j==len(words[i]) or hashMap[words[i][j]] < hashMap[words[i+1][j]]:
                    break

        return True