class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def checkWord(word):
            for i in range(1,len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if (prefix in hashSet and suffix in hashSet) or (prefix in hashSet and checkWord(suffix)):
                    return True
                        
        hashSet = set(words)
        res = []
        for word in words:
            hashSet.remove(word)
            if checkWord(word):
                res.append(word)
            hashSet.add(word)
        return res