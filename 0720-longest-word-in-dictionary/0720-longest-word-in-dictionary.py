class Solution:
    def longestWord(self, words: List[str]) -> str:
        def checkPrefixes(word):
            for i in range(len(word)):
                if word[:i+1] not in Set:
                    return False
            return True
        Set = set(words)
        pivot = ""
        for word in words:
            if checkPrefixes(word) and len(word) >= len(pivot):
                pivot = word if len(word) > len(pivot) else min(pivot,word)
        return pivot        
                